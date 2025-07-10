#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
crawler_monthly.py

每月爬取一次最新可用月份数据，然后在 MySQL 中新建
jiaoche_n, suv_n, mpv_n, all_n 四张表，n 为下一个序号。
"""

import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from sqlalchemy import create_engine, text

# —— 配置区 ——
DB_URI            = "mysql+pymysql://root:root@192.168.158.128:3306/dczj?charset=utf8mb4"
CHROMEDRIVER_PATH = r"C:\Users\LENOVO\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
MAX_LOOKBACK      = 12   # 最多回溯几个月

# 中文类型到英文表名前缀
TYPES = {
    '轿车': 'jiaoche',
    'SUV':  'suv',
    'MPV':  'mpv',
}
CATEGORY_DICT = {
    '轿车': '1-1-1%2C2%2C3%2C4%2C5%2C6',
    'SUV':  '1-1-16%2C17%2C18%2C19%2C20',
    'MPV':  '1-1-21%2C22%2C23%2C24',
}
# 用已有表当模板
TEMPLATE = {
    'jiaoche': 'jiaoche_01',
    'suv':     'suv_01',
    'mpv':     'mpv_01',
    'all':     'all_05'
}

def fetch_page(url: str):
    opts = Options()
    opts.add_argument('--headless')
    opts.add_argument('--disable-gpu')
    svc = Service(CHROMEDRIVER_PATH)
    drv = webdriver.Chrome(service=svc, options=opts)
    try:
        drv.get(url)
        time.sleep(2)
        h = drv.execute_script("return document.body.scrollHeight")
        for y in range(0, h, 500):
            drv.execute_script(f"window.scrollTo(0, {y});")
            time.sleep(0.2)
        time.sleep(1)
        return drv.current_url, drv.page_source
    finally:
        drv.quit()

def parse_blocks(html: str, label: str):
    soup = BeautifulSoup(html, 'lxml')
    rows = []
    for blk in soup.select('div.tw-relative.tw-cursor-pointer.tw-rounded.tw-border-b.tw-bg-white.tw-pr-4')[:50]:
        r = blk.select_one('div.tw-text-xl')
        n = blk.select_one('div.tw-text-nowrap.tw-text-lg')
        sd = blk.find('div', class_='tw-mb-0.5')
        sales = sd.find('span').text.strip() if sd and sd.find('span') else None
        sc = blk.select_one('strong.tw-font-bold')
        score = sc.text.strip() if sc else None
        price = ''
        for tag in blk.select('div.tw-font-medium[class*="tw-text-"]'):
            t = tag.text.strip()
            if '-' in t and '万' in t:
                price = t; break
        img = blk.select_one('img')
        img_url = img.get('data-src') or img.get('src') or '' if img else ''
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
        rows.append({
            'car_type': label,
            'ranking': int(r.text.strip()) if r else None,
            'car_name': n.text.strip() if n else None,
            'sales': int(sales.replace(',','')) if sales else None,
            'rating': float(score) if score else None,
            'price_range': price,
            'image_url': img_url
        })
    return rows

def next_suffix(conn, prefix: str) -> int:
    """
    查找 TABLE_NAME LIKE '{prefix}_%' 的最大后缀，返回 max+1。
    prefix: 'jiaoche', 'suv', 'mpv', or 'all'
    """
    sql = text(f"""
        SELECT MAX(CAST(SUBSTRING_INDEX(TABLE_NAME, '_', -1) AS UNSIGNED)) 
          FROM information_schema.TABLES
         WHERE TABLE_SCHEMA = DATABASE()
           AND TABLE_NAME LIKE :pat
    """)
    pat = f"{prefix}_%"
    mx = conn.execute(sql, {"pat": pat}).scalar() or 0
    return mx + 1

def create_table_like(conn, new_table: str, template: str):
    conn.execute(text(f"CREATE TABLE `{new_table}` LIKE `{template}`;"))

def insert_records(conn, table: str, df: pd.DataFrame):
    df.to_sql(table, conn, if_exists='append', index=False)

def main():
    engine = create_engine(DB_URI, echo=False)

    # 1. 回溯查找最新可用月
    latest = None
    for i in range(MAX_LOOKBACK + 1):
        ym = (datetime.now() - relativedelta(months=i)).strftime("%Y-%m")
        print(f"[{datetime.now()}] 测试 {ym}")
        ok = True; data = {}
        for label, seg in CATEGORY_DICT.items():
            url = f"https://www.autohome.com.cn/rank/{seg}-0_9000-x-x-x/{ym}.html"
            real, html = fetch_page(url)
            if not real.endswith(f"/{ym}.html"):
                ok = False; break
            rows = parse_blocks(html, label)
            if not rows:
                ok = False; break
            data[label] = rows
        if ok:
            latest = (ym, data)
            print("✅ 选定最新月份：", ym)
            break

    if not latest:
        print("未找到可用月份，退出。")
        return

    ym, data = latest

    # 2. 建表 & 插入
    with engine.begin() as conn:
        # 先计算所有后缀
        suffixes = {key: next_suffix(conn, key if key!='all' else 'all')
                    for key in ['jiaoche','suv','mpv','all']}
        print("后缀：", suffixes)
        for label, prefix in list(TYPES.items()) + [('all','all')]:
            suf = suffixes[prefix]
            new_table = f"{prefix}_{suf:02d}"
            tpl = TEMPLATE[prefix]
            print(f"→ CREATE {new_table} LIKE {tpl}")
            create_table_like(conn, new_table, tpl)
            # 构造 DataFrame
            if prefix == 'all':
                df_all = pd.concat(
                    [pd.DataFrame(data[l]).assign(car_type=l) for l in TYPES],
                    ignore_index=True
                )
                insert_records(conn, new_table, df_all)
            else:
                df = pd.DataFrame(data[label])
                insert_records(conn, new_table, df)
            print(f"   插入 {len(data.get(label, []))} 条到 {new_table}")

    print("完成。")

if __name__ == "__main__":
    main()

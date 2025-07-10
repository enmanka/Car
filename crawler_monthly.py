#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
    # —— 2. 后缀直接取“月”部分两位数 ——
    month = int(ym.split('-')[1])
    suffix_str = f"{month:02d}"
    check_table = f"all_{suffix_str}"

    with engine.connect() as conn:
        exists = conn.execute(
            text("SELECT COUNT(*) FROM information_schema.TABLES "
                 "WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = :t"),
            {"t": check_table}
        ).scalar()
        if exists and exists > 0:
            print(f"{suffix_str} 表已存在，网站数据未更新")
            return

    # —— 3. 新建表 & 插入 ——
    with engine.begin() as conn:
        for label, prefix in list(TYPES.items()) + [('all','all')]:
            new_table = f"{prefix}_{suffix_str}"
            tpl       = TEMPLATE[prefix]
            print(f"→ CREATE {new_table} LIKE {tpl}")
            create_table_like(conn, new_table, tpl)

            if prefix == 'all':
                df_all = pd.concat(
                    [pd.DataFrame(data[l]).assign(car_type=l) for l in TYPES],
                    ignore_index=True
                )
                insert_records(conn, new_table, df_all)
                print(f"   插入 {len(df_all)} 条到 {new_table}")
            else:
                df = pd.DataFrame(data[label])
                insert_records(conn, new_table, df)
                print(f"   插入 {len(df)} 条到 {new_table}")

    print("完成。")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
import re

import scrapy

from spider_house.items import PriceItem


class ExampleSpider(scrapy.Spider):
    name = 'price'
    allowed_domains = ['lianjia.com']
    start_urls = []
    file1 = open("zufang_url_list.txt", "r")  # 打开文件
    for line in file1:
        line = line.strip()  # 移除字符串头尾指定的字符（默认为空格）
        for page in range(1, 100):
            url = line + "pg{0}".format(page) + "rt200600000001/#contentList"
            if page == 1:
                url = line + "rt200600000001/#contentList"
            start_urls.append(url)
    file1.close()  # 关闭文件

    def parse(self, response):
        li_list = response.xpath("//span[@class='content__list--item-price']/em")
        data_list = []
        a = 0
        for li in li_list:
            url_item = PriceItem()
            url_item["price"] = li.xpath("./text()").extract_first()
            url_item["city"] = response.xpath("//p[@class='bread__nav__wrapper oneline']/a[2]/text()").extract_first()
            url_item["city"] = url_item["city"].strip("租房")
            url_item["qu"] = response.xpath("//div[@class='bread__nav w1150']/h1/a/text()").extract_first()
            url_item["qu"] = url_item["qu"].strip("租房")
            while '㎡' not in response.xpath("//p[@class='content__list--item--des']/text()").extract()[a]:
                a = a + 1
            a = a + 1
            url_item["area"] = response.xpath("//p[@class='content__list--item--des']/text()").extract()[a - 1]
            url_item["area"] = re.sub("\D", "", url_item["area"])
            data_list.append(url_item)
        return data_list

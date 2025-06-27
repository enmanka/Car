# -*- coding: utf-8 -*-
import re

import scrapy
from lxml import etree

from spider_house.items import ErShouFangItem


class CollectErShouFangDetailInfoSpider(scrapy.Spider):
    '''
    收集二手房详细信息
    '''
    name = 'price'
    allowed_domains = ['lianjia.com']
    start_urls = []
    file1 = open("ershoufang_url_list.txt", "r")  # 打开文件
    for line in file1:
        line = line.strip()  # 移除字符串头尾指定的字符（默认为空格）
        for page in range(1, 100):
            # 二手房分页url
            url = "{0}/pg{1}/".format(line, page)
            start_urls.append(url)
    file1.close()  # 关闭文件

    def parse(self, response):
        li_list = response.xpath("//div[@class='priceInfo']")
        data_list = []
        for li in li_list:
            url_item = ErShouFangItem()
            url_item["total_price"] = li.xpath("./div[@class='totalPrice']/span/text()").extract_first()
            url_item["per_price"] = li.xpath("./div[@class='unitPrice']/span/text()").extract_first()
            url_item["per_price"] = url_item["per_price"].strip('单价元/平米')
            url_item["area"] = int(url_item["total_price"]) * 10000 / int(url_item["per_price"])
            url_item["area"] = int(url_item["area"])
            url_item["area"] = str(url_item["area"])
            url_item["qu"] = response.xpath("//div[@class='crumbs fl']/h1/a/text()").extract_first()
            url_item["qu"] = url_item["qu"].strip("二手房")
            city = response.xpath("//div[@class='crumbs fl']/a[2]/text()").extract_first()
            city = city.strip("二手房")
            url_item["city"] = city
            data_list.append(url_item)
        return data_list

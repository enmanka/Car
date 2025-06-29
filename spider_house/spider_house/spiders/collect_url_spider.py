# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
import json
from random import choice

# 这个爬虫用于从链家网获取所有二手房的url

from spider_house.spider_house.items import UrlItem

cities = ['hf', 'cq', 'fz', 'gz', 'gy', 'nn', 'lz', 'wh', 'cs', 'sjz', 'hk', 'zz', 'hrb', 'nj', 'cc', 'nc', 'sy',
          'hhht', 'yinchuan', 'sh', 'cd', 'jn', 'xa', 'ty', 'tj', 'km', 'hz']


def delete_substr(in_str, in_substr):
    start_loc = in_str.find(in_substr)
    in_str, in_substr = list(in_str), list(in_substr)
    [len_str, len_substr] = len(in_str), len(in_substr)
    res_str = in_str[:start_loc]
    for i in range(start_loc + len_substr, len_str):
        res_str.append(in_str[i])
    res = ''.join(res_str)
    return res


class CollectUrlSpider(scrapy.Spider):
    name = 'myurl'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/']
    for city in cities:
        url = 'https://{city}.lianjia.com/ershoufang/'.format(city=city)
        start_urls.append(url)
    print(start_urls)

    def parse(self, response):

        html = response.text
        html_obj = etree.HTML(html)
        li_list = response.xpath(
            "/html/body/div[3]/div[@class='m-filter']/div[@class='position']/dl[2]/dd/div[1]/div/a")
        data_list = []
        for li in li_list:
            url_item = UrlItem()
            url_item["myurl"] = li.xpath("./@href").extract_first()
            url_item["myurl"] = delete_substr(url_item["myurl"], "/ershoufang/")

            url_item["qu"] = li.xpath("./text()").extract_first()
            url_item["ershou_url"] = response.xpath(
                "//div[@class='container']/ul[@class='channelList']/li[@class='selected']/a/@href").extract_first()
            url_item["ershou_url"] = delete_substr(url_item["ershou_url"], "ershoufang/")
            print(url_item["ershou_url"])
            url_item["ershou_url"] = url_item["ershou_url"] + "zufang/"
            city = response.xpath("//div[@class='crumbs fl']/h1/a/text()").extract_first()
            city = delete_substr(city, "二手房")
            url_item["city"] = city
            # content = response
            # result = json.loads(content)
            # print(result['msg'])
            data_list.append(url_item)

        print(data_list)

        return data_list

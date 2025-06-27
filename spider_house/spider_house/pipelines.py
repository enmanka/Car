# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from spider_house.items import UrlItem, ErShouFangItem, PriceItem


class SpiderHousePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, UrlItem):
            obj = ScrapyUrlPipeline()
            obj.process_item(item, spider)
        elif isinstance(item, ErShouFangItem):
            obj = ScrapyErShouFangPipeline()
            obj.process_item(item, spider)
        elif isinstance(item, PriceItem):
            obj = ScrapyZuPricePipeline()
            obj.process_item(item, spider)


# 生成二手房的url
class ScrapyUrlPipeline(object):
    def process_item(self, item, spider):
        # 注意：二手房页面链接和租房页面链接对比：
        # https://hf.lianjia.com/zufang/yaohai/
        # https://hf.lianjia.com/ershoufang/yaohai/
        # 因此获取租房链接url不必另外写爬虫，直接将ershoufang替换为zufang即可
        with open("ershoufang_url_list.txt", "a", errors='ignore') as file:
            file.write(
                item["ershou_url"] + item["myurl"] + "\n")
        return item


# 生成二手房的详细数据
class ScrapyErShouFangPipeline(object):
    def process_item(self, item, spider):
        with open("ershoufang_price.txt", "a", errors='ignore') as file:
            file.write(
                item["city"] + item["qu"] + "," + item["total_price"] + "," + item["per_price"] + "," + item[
                    "area"] + "\n")
        return item


# 生成租房数据
class ScrapyZuPricePipeline(object):
    def process_item(self, item, spider):
        with open("crawl_zufang_price.txt", "a", errors='ignore') as file:
            file.write(
                item["city"] + "," + item["qu"] + "," + item["area"] + "," + item["price"] + "\n")
        return item

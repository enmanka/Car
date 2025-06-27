# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


import scrapy


class UrlItem(scrapy.Item):
    myurl = scrapy.Field()
    city_url = scrapy.Field()
    city = scrapy.Field()
    qu = scrapy.Field()
    ershou_url = scrapy.Field()


class ErShouFangItem(scrapy.Item):
    # 城市
    city = scrapy.Field()
    # 区域
    qu = scrapy.Field()
    # 总价
    total_price = scrapy.Field()
    # 平米单价
    per_price = scrapy.Field()
    # 面积
    area = scrapy.Field()



class PriceItem(scrapy.Item):
    # 城市
    city = scrapy.Field()
    # 区域
    qu = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 价格
    price = scrapy.Field()

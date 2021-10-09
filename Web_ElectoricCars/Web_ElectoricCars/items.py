# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebElectoriccarsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    CarName = scrapy.Field()
    BrandNewCarPrice = scrapy.Field()
    UsedCarPrice = scrapy.Field()
    URL = scrapy.Field()

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebScrapingTradingcompanyItem(scrapy.Item):
    Company = scrapy.Field()
    Industry = scrapy.Field()
    Location = scrapy.Field()
    Description = scrapy.Field()
    URL = scrapy.Field()
    
    

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebScUniversitiesUkItem(scrapy.Item):
    Program = scrapy.Field()
    University = scrapy.Field()
    EducationLevel = scrapy.Field()
    Location = scrapy.Field()
    Term = scrapy.Field()
    Method = scrapy.Field()
    URL = scrapy.Field()

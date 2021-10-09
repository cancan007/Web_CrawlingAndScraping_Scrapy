import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Web_Sc_Universities_UK.item import UK_Universities
from Web_UKPrograms.items import WebUkprogramsItem


class UkUniversitiesSpider(CrawlSpider):
    name = 'UK_Universities'
    allowed_domains = ['educations.com']
    start_urls = ['https://www.educations.com/search/tourism-hospitality-england/c421-d87257',
                  'https://www.educations.com/search/tourism-hospitality-england/c421-d87257?page=2',
                  'https://www.educations.com/search/tourism-hospitality-england/c421-d87257?page=3]',
                  'https://www.educations.com/search/tourism-hospitality-england/c421-d87257?page=4',
                  'https://www.educations.com/search/tourism-hospitality-england/c421-d87257?page=5',
                  'https://www.educations.com/search/tourism-hospitality-england/c421-d87257?page=6',
                  'https://www.educations.com/search/tourism-hospitality-england/c421-d87257?page=7']
                  
"""
    rules = (
        Rule(LinkExtractor(restrict_css=' div > span.pager-item.pager-item-nav.pager-item-hover > a'), callback='parse_item', follow=True),
    )
"""
"""
    def parse_item(self, response):
        for col in response.css('div.emg-serp__serp-container > div.emg-serp__row.emg-serp__row-has-compare'):
            item = WebScUniversitiesUkItem()
            item['Program'] = col.css(' div > div.emg-serp-item__title-text::text').get()
            item['University'] = col.css('div.emg-serp-item__row.emg-serp-item__row-subtitle > div::text').get()
            item['EducationLevel'] = col.css('li.emg-serp-item__flag.emg-serp-item__flag-type.emg-serp-item__flag-0 > div > span::text').get()
            item['Location'] = col.css('li.emg-serp-item__flag.emg-serp-item__flag-place.emg-serp-item__flag-1 > div > span::text').get()
            item['Term'] = col.css(' li.emg-serp-item__flag.emg-serp-item__flag-length.emg-serp-item__flag-2 > div > span::text').get()
            item['Method'] = col.css('li.emg-serp-item__flag.emg-serp-item__flag-deliverymethod.emg-serp-item__flag-3 > div > span::text').get()
            item['URL'] = col.css('a.emg-serp__link::attr(href)').get()
            yield item
            
    def parse_start_url(self, response):
        return self.parse_item(response)
"""

    def parse(self, response):
        for col in response.css('div.emg-serp__serp-container > div.emg-serp__row.emg-serp__row-has-compare'):
            item = WebUkprogramsItem()
            item['Program'] = col.css(' div > div.emg-serp-item__title-text::text').get()
            item['University'] = col.css('div.emg-serp-item__row.emg-serp-item__row-subtitle > div::text').get()
            item['EducationLevel'] = col.css('li.emg-serp-item__flag.emg-serp-item__flag-type.emg-serp-item__flag-0 > div > span::text').get()
            item['Location'] = col.css('li.emg-serp-item__flag.emg-serp-item__flag-place.emg-serp-item__flag-1 > div > span::text').get()
            item['Term'] = col.css(' li.emg-serp-item__flag.emg-serp-item__flag-length.emg-serp-item__flag-2 > div > span::text').get()
            item['Method'] = col.css('li.emg-serp-item__flag.emg-serp-item__flag-deliverymethod.emg-serp-item__flag-3 > div > span::text').get()
            item['URL'] = col.css('a.emg-serp__link::attr(href)').get()
            yield item

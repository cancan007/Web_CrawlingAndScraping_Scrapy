import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Web_Scraping_TradingCompany.items import WebScrapingTradingcompanyItem


class TradingCompaniesSpider(CrawlSpider):
    name = 'trading_companies'
    allowed_domains = ['baseconnect.in']
    start_urls = ['https://baseconnect.in/companies/keyword/2a970ee1-15a7-45e0-b1eb-37e738712447/']

    rules = (
        Rule(LinkExtractor(restrict_css=' div > a.next_page'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for com in response.css(' div.searches__result > div.searches__result__list'):
            item = WebScrapingTradingcompanyItem()
            item['Company'] = com.css('div.searches__result__list__header.cf > h4 > a::text').extract_first()
            item['Industry'] = com.css('ul > li.searches__tag.searches__tag--listed > a::text').extract()
            item['Location'] = com.css('div.searches__result__list__conts__text > p.searches__result__list__conts__text__address::text').extract_first()
            item['Description'] = com.css('div.searches__result__list__conts__text > h5::text').extract_first()
            item['URL'] = 'https://baseconnect.in/companies/keyword/2a970ee1-15a7-45e0-b1eb-37e738712447' + com.css(' div.searches__result__list__header.cf > h4 > a::attr(href)').extract_first()
            yield item
            
    def parse_start_url(self, response):
        return self.parse_item(response)

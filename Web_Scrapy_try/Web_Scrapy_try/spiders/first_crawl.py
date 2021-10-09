import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Web_Scrapy_try.items import WebScrapyTryItem


class FirstCrawlSpider(CrawlSpider):
    name = 'first_crawl'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        Rule(
            LinkExtractor(restrict_css=' ul > li.next > a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for quote in response.css('div.quote'):
            item = WebScrapyTryItem()
            item['author'] = quote.css('small.author::text').extract_first()
            item['text'] = quote.css('span.text::text').extract_first()
            item['tags'] = quote.css('div.tags a.tag::text').extract()
            yield item
    
    def parse_start_url(self, response):
        return self.parse_item(response)

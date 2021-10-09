import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Web_ElectoricCars.items import WebElectoriccarsItem


class ForElectricCarsSpider(CrawlSpider):
    name = 'for_electric_cars'
    allowed_domains = ['kakaku.com']
    #allowed_domains = ['kakaku.com/kuruma/ranking/fueltype=electric-car/', 'kakaku.com', 'https://kakaku.com/kuruma/ranking/fueltype=electric-car/page=2']
    start_urls = ['https://kakaku.com/kuruma/ranking/fueltype=electric-car/']
    #start_urls = ['https://kakaku.com/kuruma/ranking/fueltype=electric-car/page=1/']

    rules = (
        Rule(LinkExtractor(restrict_css='ul > li.next > a'),         callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for car in response.css('div.rkgContents.v2> div.rkgBox.noGraph'):
        #for car in response.css('div.rkgContents.v2'):
            item = WebElectoriccarsItem()
            item['CarName'] = car.css('div > a.rkgBoxType::text').extract_first()
            item['BrandNewCarPrice'] = car.css('span.price > a::text').extract_first()
            item['UsedCarPrice'] = car.css('div.rkgRow.rowUpper.upperSpace2 > div:nth-child(3) > span.price > a::text').extract_first()
            item['URL'] = 'https://kakaku.com/kuruma/ranking/fueltype=electric-car' + car.css(' div > a.rkgBoxType::attr(href)').extract_first()
            yield item
            
    def parse_start_url(self, response):
        return self.parse_item(response)
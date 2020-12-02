import scrapy
from ..items import  SpideritviecItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://itviec.com/viec-lam-it-theo-ten-cong-ty',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = SpideritviecItem()

        all_categories_name = response.css('a.skill-tag__link::text').extract().sripe()
        for name in all_categories_name:
            items['name'] = name
            yield items


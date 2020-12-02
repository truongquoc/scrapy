import scrapy
from ..items import SpideritviecItem

class QuotesSpider(scrapy.Spider):
    name = "profile"

    def start_requests(self):
        urls = [
            'https://itviec.com/it-jobs/da-nang',
            'https://itviec.com/it-jobs/da-nang?page=2'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for href in response.css('.title > a::attr("href")'):
             next_page = response.urljoin(href.extract())
             yield scrapy.Request(next_page, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = SpideritviecItem()
        name = response.css('.name > a::text').get()
        image = response.css('.logo > a >img::attr("src")').get()
        address = response.css('.address__full-address > span::text').get()

        item['name'] = name
        item['logoImage'] = image
        item['address'] = address
        yield item

import scrapy
from ..items import SpideritviecItem

class QuotesSpider(scrapy.Spider):
    name = "tags"

    def start_requests(self):
        urls = [
            'https://topdev.vn/viec-lam-it',
            'https://topdev.vn/viec-lam-it?page=2',
            'https://topdev.vn/viec-lam-it?page=3',
            'https://topdev.vn/viec-lam-it?page=4',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for href in response.css('.logo-box > a::attr("href")').extract():
             yield scrapy.Request(href, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = SpideritviecItem()
        name = response.css('.fwb::text').get().strip()
        urlImage = response.css('.img > img::attr("src")').get()
        yield {'tag':newTags}



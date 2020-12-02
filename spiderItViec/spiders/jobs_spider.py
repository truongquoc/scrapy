import scrapy
from ..items import SpideritviecItem

class QuotesSpider(scrapy.Spider):
    name = "jobs"

    def start_requests(self):
        urls = [
            'https://itviec.com/viec-lam-it/android',
            'https://itviec.com/viec-lam-it/android?page=2',
            'https://itviec.com/viec-lam-it/android?page=3'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for href in response.css('.title > a::attr("href")'):
             next_page = response.urljoin(href.extract())
             yield scrapy.Request(next_page, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = SpideritviecItem()
        name = response.css('.job_title::text').extract()[0].replace('\n', '')
        image = response.css('.logo > a >img::attr("src")').get()
        address =  response.css('.address__full-address > span::text').get()
        tags = response.css('.tag-list > a  > span::text').extract()
        newtags = [tag.replace('\n','') for tag in tags]
        description = response.css('.description > ul').extract()
        content = response.css('.experience > p+ul').extract()

        item['name'] = name;
        item['logoImage'] = image
        item['address'] = address
        item['tags'] = newtags
        item['description'] = description
        item['content'] = content
        yield item

import scrapy


class MyprojectSpider(scrapy.Spider):
    name = "project"
    allowed_domains = ["dmoz.org"]

    start_urls = [
        "https://itviec.com/viec-lam-it/android",
    ]

    def parse(self, response):
        for href in response.css(".title > a::attr('href')"):
            yield {'id':href}
            url = response.urljoin(href.extract())
            # yield {'url', url}

    def parse_dir_contents(self, response):
        for sel in response.xpath('//ul/li'):
            print('hee')
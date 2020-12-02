# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpideritviecItem(scrapy.Item):
    name = scrapy.Field()
    content = scrapy.Field()
    logoImage = scrapy.Field()
    address = scrapy.Field()
    tags = scrapy.Field()
    description = scrapy.Field()

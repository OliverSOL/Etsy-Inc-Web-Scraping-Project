# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EtsyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    prodname = scrapy.Field()
    description = scrapy.Field()
    rating = scrapy.Field()
    amountsaved = scrapy.Field()
    price = scrapy.Field()
    amountofsales = scrapy.Field()
    bestseller = scrapy.Field()



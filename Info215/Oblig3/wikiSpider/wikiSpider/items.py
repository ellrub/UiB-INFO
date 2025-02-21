# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class Article(scrapy.Item):
#     url = scrapy.Field()
#     title = scrapy.Field()
#     lastUpdated = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()

class VergeReview(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    author_name = scrapy.Field()
    author_profile_link = scrapy.Field()

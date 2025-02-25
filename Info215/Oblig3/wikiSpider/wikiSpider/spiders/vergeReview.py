from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wikiSpider.items import VergeReview

class VergeReviewSpider(CrawlSpider):
    name = 'vergeReview'

    allowed_domains = ['theverge.com']
    start_urls = ['https://www.theverge.com/reviews']

    rules = [
        Rule(LinkExtractor(allow = "https://www\.theverge\.com/(?:[a-z-]+/\d+|d+)/[^/]+"),
             callback = 'parse_items', follow = True)
        ]
    
    def parse_items(self, response):
        verge_review = VergeReview()
        verge_review['url'] = response.url
        verge_review['title'] = response.xpath('//h1/text()').extract_first()
        verge_review['author_name'] = response.xpath("//span[contains(@class, '_114qu8c2')]/a/text()").extract_first()
        verge_review['author_profile_link'] = response.xpath("//span[contains(@class, '_114qu8c2')]/a/@href").extract_first()

        yield verge_review
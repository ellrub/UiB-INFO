from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wikiSpider.items import VergeReview
from urllib.request import urljoin

class VergeReviewSpider(CrawlSpider):
    name = 'vergeReview'

    allowed_domains = ['theverge.com']
    start_urls = ['https://www.theverge.com/reviews']
    

    rules = [
        Rule(LinkExtractor(allow = r"https://www.theverge.com/\d+/[^/]+$"),
             callback = 'parse_items', follow = True)
        ]
    
    def parse_items(self, response):
        root_domain = 'https://www.theverge.com'
        verge_review = VergeReview()
        verge_review['url'] = response.url
        verge_review['title'] = response.xpath('//h1/text()').extract_first()
        verge_review['author_name'] = response.xpath("//span/a/text()").extract_first()
        verge_review['author_profile_link'] = urljoin(root_domain, response.xpath("//span/a/@href").extract_first())

        if verge_review['title'] is not None and verge_review['author_name'] is not None:
            yield verge_review
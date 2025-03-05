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
        title = response.xpath('//h1/text()').extract_first()
        author_name = response.xpath("//span/a/text()").extract_first()
        author_profile_link = urljoin(root_domain, response.xpath("//span/a/@href").extract_first())
        verge_review = VergeReview()
        verge_review['url'] = response.url

        if title is not None and author_name is not None:
            verge_review['title'] = title
            verge_review['author_name'] = author_name
            verge_review['author_profile_link'] = author_profile_link

            yield verge_review
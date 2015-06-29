from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request, HtmlResponse

from src.items import revscraperItem

class ReviewScraper (CrawlSpider):
    name = "revscraper"

    def __init__(self, product_id):
        self.counter = 0
        self.product_id = product_id
        self.allowed_domains = ["amazon.in"]

    def start_requests(self):
        for i in range(30):
            if self.counter > 100:
                break
            url = 'http://www.amazon.in/product-reviews/%s/ref=cm_cr_pr_btm_link_2?ie=UTF8&pageNumber=%d&showViewpoints=0&sortBy=byRankDescending' % (self.product_id, i)
            yield self.make_requests_from_url(url)

    def parse (self, response):
        select = Selector(response)
        item = revscraperItem()
        x = select.xpath ('//div[@class="reviewText"]/text()').extract()
        if x != []:
            self.counter += len (x)
            item['reviews'] = x
            yield item

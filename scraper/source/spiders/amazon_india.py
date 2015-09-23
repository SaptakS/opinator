from __future__ import absolute_import
from .. import items
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request, HtmlResponse

class AmazonINScraper (CrawlSpider):
    name = "amazonIN"

    def __init__(self, product_id, **kwargs):
        self.allowed_domains = ["amazon.in"]
        self.counter = 0
        self.product_id = product_id

    def start_requests(self):
        for i in range(5):
            if self.counter > 25:
                break
            url = "http://www.amazon.in/product-reviews/%s/ref=cm_cr_pr_btm_link_11?showViewpoints=1&sortBy=helpful&reviewerType=all_reviews&filterByStar=all_stars&pageNumber=%d"% (self.product_id, i)
            yield self.make_requests_from_url(url)

    def parse (self, response):

        select = Selector(response)
        item = items.scraperItem()
        x = select.xpath ('//span[@class="a-size-base review-text"]/text()').extract()
        if x != []:
            self.counter += len (x)
            item['reviews'] = x
            item['file_'] = str(self.product_id)
            yield item

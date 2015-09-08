from __future__ import absolute_import
from .. import items
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request, HtmlResponse
#from scraper.source.items import scraperItem
#import urllib, httplib

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
            url = 'http://www.amazon.in/product-reviews/%s/ref=cm_cr_pr_btm_link_2?ie=UTF8&pageNumber=%d&showViewpoints=0&sortBy=byRankDescending' % (self.product_id, i)
            yield self.make_requests_from_url(url)

    def parse (self, response):

        select = Selector(response)
        item = items.scraperItem()
        x = select.xpath ('//div[@class="reviewText"]/text()').extract()
        if x != []:
            self.counter += len (x)
            item['reviews'] = x
            item['file_'] = str(self.product_id)
            #params = urllib.urlencode({'reviews': x})
            #headers = {"Content-type": "application/json"}
            #conn = httplib.HTTPConnection ("127.0.0.1:5000")
            #conn.request("POST", "/reviews", params, headers)
            yield item

from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request, HtmlResponse
from src.items import revscraperItem
from sys import argv

class ReviewScraper (CrawlSpider):
    name = "revscraper"
    allowed_domains = ["amazon.in"]
    global counter
    global productID

    counter = 0
    productID = argv[1]

    def start_requests(self):
        global counter

        for i in range(30):
            if counter > 100:
                break
            url = 'http://www.amazon.in/product-reviews/%s/ref=cm_cr_pr_btm_link_2?ie=UTF8&pageNumber=%d&showViewpoints=0&sortBy=byRankDescending' % (productID, i)
            yield self.make_requests_from_url(url)

    def parse (self, response):
        global counter
        global productID

        select = Selector(response)
        item = revscraperItem()
        x = select.xpath ('//div[@class="reviewText"]/text()').extract()
        if x != []:
            counter += len (x)
            item['reviews'] = x
            item['product_id'] = productID
            item['website_name'] = 'amazon.in'
            yield item

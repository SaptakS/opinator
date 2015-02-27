from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request, HtmlResponse
from OpinatorScraper.items import OpinatorscraperItem
import sys

class ReviewScraper (CrawlSpider):
    name = "OpinatorScraper"
    allowed_domains = ["amazon.in"]
    global counter
    counter = 0
    def start_requests(self):
        productID = sys.argv[1]
        for i in range(30):
            global counter
            if counter > 100:
                break
            url = 'http://www.amazon.in/product-reviews/%s/ref=cm_cr_pr_btm_link_2?ie=UTF8&pageNumber=%d&showViewpoints=0&sortBy=byRankDescending' % (productID, i)
            yield self.make_requests_from_url(url)

    def parse (self, response):
        select = Selector(response)
        item = OpinatorscraperItem()
        x = select.xpath ('//div[@class="reviewText"]/text()').extract()
        if not x == []:
            global counter
            counter += len (x)
            item['reviews'] = x
            yield item

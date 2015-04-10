from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request, HtmlResponse
from OpinatorScraper.items import OpinatorscraperItem
from sys import argv

class ReviewScraper (CrawlSpider):
    name = "OpinatorScraper"
    allowed_domains = ["amazon.in"]
    global counter
    global productID

    counter = 0
    productID = argv[1]

    def start_requests(self):
<<<<<<< HEAD
        global counter
=======
        productID = argv[1]
>>>>>>> fc15b1d3997c53a290960ff4b002d6a18d7b9501
        for i in range(30):
            if counter > 100:
                break
            url = 'http://www.amazon.in/product-reviews/%s/ref=cm_cr_pr_btm_link_2?ie=UTF8&pageNumber=%d&showViewpoints=0&sortBy=byRankDescending' % (productID, i)
            yield self.make_requests_from_url(url)

    def parse (self, response):
        global counter
        global productID

        select = Selector(response)
        item = OpinatorscraperItem()
        x = select.xpath ('//div[@class="reviewText"]/text()').extract()
        if x != []:
<<<<<<< HEAD
=======
            global counter
>>>>>>> fc15b1d3997c53a290960ff4b002d6a18d7b9501
            counter += len (x)
            item['reviews'] = x
            item['product_id'] = productID
            item['website_name'] = 'amazon.in'
            yield item

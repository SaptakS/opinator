from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request, HtmlResponse
import scrapy.item

class wikiSpider (CrawlSpider):
    name = "OpinatorScraper"
    allowed_domains = ["amazon.in"]
    start_urls = ["http://www.amazon.in/gp/product/1473605202/"]
    rules = (
        Rule(LxmlLinkExtractor(restrict_xpaths = ("//div[@id = 'detail_bullets_id']"), allow = ("(http)(:)(/)(/)(www.amazon.in)(/)(product)(-)(reviews)(/)")), callback = 'parse_item', ),
    )

    def parse_item (self, response):
        x = Selector(response=response).xpath('//div[@class="reviewText"]/text()').extract()
        x = str(x)
        f = open ("sachinWiki.json", "w")
        f.write(x)

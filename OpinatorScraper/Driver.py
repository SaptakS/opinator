#!/usr/bin/env python
from scrapy.cmdline import execute
pID = str(1473605202)
execute (['scrapy', 'crawl', 'OpinatorScraper', '-o', 'reviews.json'])

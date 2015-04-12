#!/usr/bin/env python
from scrapy.cmdline import execute

execute (['scrapy', 'crawl', 'OpinatorScraper', '-t' , 'json'])

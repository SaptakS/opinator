# -*- coding: utf-8 -*-

# Scrapy settings for OpinatorScraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:



BOT_NAME = 'OpinatorScraper'

SPIDER_MODULES = ['OpinatorScraper.spiders']
NEWSPIDER_MODULE = 'OpinatorScraper.spiders'

<<<<<<< HEAD
DATABASE = {
    'drivername': 'mysql',
    'host': 'localhost',
    'port': '3306',
    'username': 'vivek',
    'password': 'vivek',
    'database': 'op12'
}

ITEM_PIPELINES = ['OpinatorScraper.pipelines.OpinatorscraperPipeline']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'OpinatorScraper (+http://www.yourdomain.com)'
=======
>>>>>>> fc15b1d3997c53a290960ff4b002d6a18d7b9501

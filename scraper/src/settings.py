# -*- coding: utf-8 -*-

# Scrapy settings for OpinatorScraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:



BOT_NAME = 'OpinatorScraper'

SPIDER_MODULES = ['OpinatorScraper.spiders']
NEWSPIDER_MODULE = 'OpinatorScraper.spiders'

DATABASE = {
    'drivername': 'mysql',
    'host': 'localhost',
    'port': '3306',
    'username': 'vivek',
    'password': 'vivek',
    'database': 'op12'
}

ITEM_PIPELINES = ['OpinatorScraper.pipelines.OpinatorscraperPipeline']

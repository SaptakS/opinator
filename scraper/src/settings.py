# -*- coding: utf-8 -*-

# Scrapy settings for OpinatorScraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:



BOT_NAME = 'revscraper'

SPIDER_MODULES = ['src.spiders']
NEWSPIDER_MODULE = 'src.spiders'

DATABASE = {
    'drivername': 'mysql',
    'host': 'localhost',
    'port': '3306',
    'username': 'vivek',
    'password': 'vivek',
    'database': 'op12'
}

ITEM_PIPELINES = ['src.pipelines.revscraperPipeline']

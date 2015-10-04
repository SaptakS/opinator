import os

BOT_NAME = 'scraper'

SPIDER_MODULES = ['source.spiders']

ITEM_PIPELINES = {
'source.pipelines.scraperPipeline' : 300
}

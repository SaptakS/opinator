import os

BOT_NAME = 'scraper'

SPIDER_MODULES = ['source.spiders']

ITEM_PIPELINES = {
'source.pipelines.scraperPipeline' : 300
}

try:
    BROKER_HOST = os.environ['BROKER_HOST']
except KeyError:
    BROKER_HOST = 'localhost'

try:
    BROKER_PORT = os.environ['BROKER_PORT']
except KeyError:
    BROKER_PORT = 5672

try:
    BROKER_USERID = os.environ['BROKER_USERID']
except KeyError:
    BROKER_USERID = 'guest'

try:
    BROKER_PASSWORD = os.environ['BROKER_PASSWORD']
except KeyError:
    BROKER_PASSWORD = 'guest'

try:
    BROKER_VIRTUAL_HOST = os.environ['BROKER_VIRTUAL_HOST']
except KeyError:
    BROKER_VIRTUAL_HOST = '/'

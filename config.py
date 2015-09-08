import os

basedir = os.path.abspath(os.path.dirname(__file__))

# The number of days for which the sentiment is valid
LIFESPAN = 0

# Mapping of website_name to class name for table in db
#from app import models
#WEBSITE_TO_CLASS = {'amazon.in': AmazonIN}

# Mapping of website_name to spider name
#WEBSITE_TO_SPIDER = {'amazon.in': 'amazonIN'}

SQLALCHEMY_DATABASE_URI = 'mysql://vivek:vivek@localhost/op20'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

"""
try:
    BROKER_HOST = os.environ['BROKER_HOST']
except:
    BROKER_HOST = 'localhost'

try:
    BROKER_PORT = os.environ['BROKER_PORT']
except:
    BROKER_PORT = 5672

try:
    BROKER_USERID = os.environ['BROKER_USERID']
except:
    BROKER_USERID = 'guest'

try:
    BROKER_PASSWORD = os.environ['BROKER_PASSWORD']
except KeyError:
    BROKER_PASSWORD = 'guest'

try:
    BROKER_VIRTUAL_HOST = os.environ['BROKER_VIRTUAL_HOST']
except KeyError:
    BROKER_VIRTUAL_HOST = '/'

try:
    SCRAPYD_HOST = os.environ['SCRAPYD_HOST']
except KeyError:
    SCRAPYD_HOST = 'localhost'

try:
    SCRAPYD_PORT = os.environ['SCRAPYD_PORT']
except KeyError:
    SCRAPYD_PORT = '6800'

"""

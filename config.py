import os

basedir = os.path.abspath(os.path.dirname(__file__))

# The number of days for which the sentiment is valid
LIFESPAN = 0 

# Mapping of website_name to spider name
WEBSITE_TO_SPIDER = {'amazon.in': 'amazonIN'}

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<user>:<pass>@localhost/opinator'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

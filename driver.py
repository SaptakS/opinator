import sys
from subprocess import call
from cgi import FieldStorage
sys.path.insert(0, '/home/vivek/opinator/database')
from dbdriver import driver

data = FieldStorage()
product_id = str(data.getvalue('product_code'))
website_name = str(data.getvalue('website'))
url = str(data.getvalue('url'))

status, sentiment = driver(website_name=website_name, product_id=product_id, action='query')

update_flag = 0
if status == 'outdated':
    update_flag = 1
elif status == 'present':
    #return 'sentiment' to plugin code
    pass
elif status == 'absent':
    #this implies the product is new
    pass

call(['python', '/var/www/html/opinator/scraper/driver.py', product_id])
sentiment_score, sentiment = call(['python', '/var/www/html/opinator/mindwrap/sentiment.py'])

#################
#code to return sentiment to the plugin goes here
################

#update the database
if update_flag == 1:
    driver(website_name=website_name, product_id=product_id, action='update', url=url,
            sentiment_score=sentiment_score, sentiment=sentiment)
else:
    driver(website_name=website_name, product_id=product_id, action='insert', url=url,
            sentiment_score=sentiment_score, sentiment=sentiment)

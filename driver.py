import sys
from subprocess import Popen
from flask import Flask, request

sys.path[:0] = ['/var/www/html/opinator/database', '/var/www/html/opinator/mindwrap']
from driver import Driver
from sentiment import sentiment_calculator


app = Flask(__name__)

@app.route('/', methods=['POST'])
def drive():
    product_id = request.json['product_id']
    url = request.json['url']
    website_name = request.json['website_name']

    query_obj = Driver(website_name=website_name, product_id=product_id, action='query')
    status, sentiment = query_obj.drive()

    update_flag = 0
    if status == 'outdated':
        # The product has been searched before but is outdated
        update_flag = 1
    elif status == 'present':
        # The product is present in the database and there is no need of
        # further actions
        return sentiment
    elif status == 'absent':
        # this implies the product is new

    # Run the scraper
    p = Popen(['scrapy', 'crawl', '-a', 'product_id=%s' % product_id , 'revscraper'], cwd='/var/www/html/opinator/scraper')
    p.wait()

    # sentiment_calculator() is function which uses coreNLP to give back
    # sentiment_score and sentiment
    sentiment_score, sentiment = sentiment_calculator()

    #update the database
    if update_flag == 1:
        # Update the database with the new sentiment scores and sentimet of the
        # earlier existing product
        update_obj = Driver(website_name=website_name, product_id=product_id, action='update', url=url,
                                sentiment_score=sentiment_score, sentiment=sentiment)
        update_obj.drive()
    else:
        # Update the database with a new product
        insert_obj = Driver(website_name=website_name, product_id=product_id, action='insert', url=url,
                                sentiment_score=sentiment_score, sentiment=sentiment)
        insert_obj.drive()

    return sentiment

# Run the flask server
app.run(debug=True)

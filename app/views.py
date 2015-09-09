from flask import request
from flask.json import jsonify
from datetime import datetime, timedelta
import scrapy
#from scrapy.crawler import CrawlerProcess
import os
from app import app, db
from sentiment import StanfordNLP, VALUES
from .models import *
from config import LIFESPAN

#from twisted.internet import reactor

#from scrapy import log, signals
#from scrapy.crawler import Crawler
#from scrapy.settings import Settings
#from scrapy.xlib.pydispatch import dispatcher

def stop_reactor():
    reactor.stop()

def is_present(website_name, product_id):
    """Checks if the product is already present in the database,
        Return the product object if it is present and None if
        it isn't.
    """
    return AmazonIN.query.filter(AmazonIN.product_id==product_id).first()

def is_valid(product):
    """Checks if the product's date of view has expired
        or not. This function assumes that the product is
        already present in the database. The product's validity
        is checked on the basis of a config varialbe: 'LIFESPAN',
        which simply stands for the number of days the sentiment
        is valid.

        Returns 'True' is the product is valid, 'False' if not.
    """
    current_datetime = datetime.now()
    valid_modified_on = current_datetime - timedelta(days=LIFESPAN)

    if valid_modified_on <= product.modified_on:
        return True
    else:
        return False

def insert(website_name, product_id, url,
            sentiment_score, sentiment):
    """Inserts in the database"""

    new_product = AmazonIN(product_id=product_id, url=url,
                            sentiment_score=sentiment_score,
                            sentiment=sentiment, added_on=datetime.now(),
                            modified_on=datetime.now())
    db.session.add(new_product)
    db.session.commit()
    return

def update(website_name, product_id, url,
            sentiment_score, sentiment):
    """Updates the database"""

    product = is_present(website_name, product_id)
    product.sentiment_score = sentiment_score
    product.sentiment = sentiment
    product.modified_on = datetime.now()
    db.session.commit()
    return

def recieve_reviews(reviews):
    new_rev = ''
    for i in reviews:
        i.encode('utf-8')
        new_rev += i

    #print new_rev
    nlp = StanfordNLP()
    results = nlp.parse(new_rev)
    #print results
    results = results['sentences']
    #print results
    value = 0
    count = 0
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    very_positive_count = 0
    very_negative_count = 0
    for result in results:
        count += 1
        #print result['sentiment']
        if result['sentiment'] == "Negative":
            negative_count += 1
        elif result['sentiment'] == "Very Negative":
            very_negative_count += 1
        elif result['sentiment'] == "Positive":
            positive_count += 1
        elif result['sentiment'] == "Very Positive":
            very_positive_count += 1
        else:
            neutral_count += 1

        value = value + VALUES[result['sentiment']]
        #print "While assigning value"
    if count:
        value = float(value / (count * 1.0))

    #print "value is: ", value
    if value <= -1:
        result = 'Negative'
    elif value > -0.5:
        result = 'Positive'
        value = abs(value)
    else:
        result = 'Neutral'

    #print(result)
    return (value, result, positive_count, negative_count,
                very_positive_count, very_negative_count, neutral_count)

@app.route('/', methods=['POST'])
def plugin_response_handler():
    """It does all the talking with the plugin"""

    # Recieving data from the plugin
    product_id = request.json['product_id']
    url = request.json['url']
    website_name = request.json['website_name']
    #print 'getting ', product_id, website_name


    outdated = False
    product = is_present(website_name, product_id)
    if product is not None:
        if is_valid(product):
            return jsonify(sentiment_score=str(product.sentiment_score),
                                    sentiment=product.sentiment)
        else:
            outdated = True

    '''
    ################## Running scrapy from script code ################
    #dispatcher.connect(stop_reactor, signal=signals.spider_closed)
    #spider = FollowAllSpider(domain='scrapinghub.com')
    spider = AmazonINScraper(product_id)
    crawler = Crawler(Settings())
    crawler.signals.connect(reactor.stop, signal=signals.item_scraped)
    crawler.configure()
    crawler.crawl(spider)
    print 'after crawler.crawl'
    crawler.start()
    log.start()
    log.msg('Running reactor...')
    reactor.run(installSignalHandlers=False)  # the script will block here until the spider is closed
    log.msg('Reactor stopped.')
    print 'after stopping of reactor'
    '''

    cmd = "scrapy crawl %s -a product_id=%s" % (website_name, product_id)
    print 'present working directory', os.getcwd()
    #os.chdir("/home/vivek/temp/opinator4/app/scraper")
    os.chdir("./scraper")
    os.system(cmd)
    #print 'after scrapy'
    with open('%s.txt' % str(product_id), 'r') as f:
        #print f.read()
        (value, result, positive_count, negative_count, very_positive_count,
                very_negative_count, neutral_count) = recieve_reviews(f.read())
    os.chdir("..")
    if outdated:
        update(website_name=website_name, product_id=product_id, url=url,
                sentiment_score=value, sentiment=str(result))
    else:
        insert(website_name=website_name, product_id=product_id, url=url,
                sentiment_score=value, sentiment=str(result))

    return jsonify(sentiment_score=str(value), sentiment=str(result), positive_count=str(positive_count),
                    negative_count=str(negative_count), very_positive_count=str(very_positive_count),
                        very_negative_count=str(very_negative_count), neutral_count=str(neutral_count))

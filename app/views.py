import scrapy
import os
from flask import request
from flask.json import jsonify
from datetime import datetime, timedelta

from app import app, db
from sentiment import StanfordNLP, VALUES
from .models import *
from config import LIFESPAN

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
        is checked on the basis of a config variable: 'LIFESPAN',
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
    """Inserts new product in the database"""

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

def calculate_sum_sentiments(results):
    """Calculates the sum of the sentiments.
        Each type of sentiment is assigned some value
        in the VALUES dictionary
    """

    value, count = 0, 0
    positive_count, negative_count, neutral_count = 0, 0, 0
    very_positive_count, very_negative_count = 0, 0
    for result in results:
        count += 1
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
    return (count, value, positive_count, negative_count, neutral_count,
            very_positive_count, very_negative_count)

def categorize_sentiment(value):
    """Categorizes sentiment on the basis of
        sentiment values
    """

    if value <= -1:
        result = 'Negative'
    elif value > -0.5:
        result = 'Positive'
        value = abs(value)
    else:
        result = 'Neutral'
    return result

def calculate_sentiment(reviews):
    """Calculates the overall sentiment of the reviews"""

    #encoding reviews
    new_rev = ''
    for i in reviews:
        i.encode('utf-8')
        new_rev += i

    #getting the sentiment results
    #from the analyzer module
    nlp = StanfordNLP()
    results = nlp.parse(new_rev)
    results = results['sentences']


    (count, value, positive_count, negative_count, neutral_count,
            very_positive_count, very_negative_count) = calculate_sum_sentiments(results)

    if count:
        sentiment_value = float(value / (count * 1.0))

    overall_sentiment = categorize_sentiment(sentiment_value)

    return (sentiment_value, overall_sentiment, positive_count, negative_count,
                very_positive_count, very_negative_count, neutral_count)

@app.route('/', methods=['POST'])
def plugin_response_handler():
    """It does all the talking with the plugin"""

    # Recieving data from the plugin
    product_id = request.json['product_id']
    url = request.json['url']
    website_name = request.json['website_name']

    #checking if the product was already analyzed
    outdated = False
    product = is_present(website_name, product_id)
    if product is not None:
        if is_valid(product):
            return jsonify(sentiment_score=str(product.sentiment_score),
                                    sentiment=product.sentiment)
        else:
            outdated = True

    #If it is not already analyzed, scraper is called
    cmd = "scrapy crawl %s -a product_id=%s" % (website_name, product_id)
    os.chdir("./scraper")

    #execution of the scraper
    os.system(cmd)

    #the scraper pipelines the reviews to a text file, named as product_id
    with open('%s.txt' % str(product_id), 'r') as f:

        #read in the reviews and analyze the data
        (value, result, positive_count, negative_count, very_positive_count,
                very_negative_count, neutral_count) = calculate_sentiment(f.read())
    os.chdir("..")

    #update the database if necessary otherwise, add a new product to the db
    if outdated:
        update(website_name=website_name, product_id=product_id, url=url,
                sentiment_score=value, sentiment=str(result))
    else:
        insert(website_name=website_name, product_id=product_id, url=url,
                sentiment_score=value, sentiment=str(result))

    #return the json object to the plugin
    return jsonify(sentiment_score=str(value), sentiment=str(result), positive_count=str(positive_count),
                    negative_count=str(negative_count), very_positive_count=str(very_positive_count),
                        very_negative_count=str(very_negative_count), neutral_count=str(neutral_count))

from update import update
from query import query
from insert import insert
from dbsettings import LIFESPAN
from datetime import datetime, timedelta

def query_handler(website_name, product_id):
    """Handler function for query before scraping"""

    #query for given website_name and product_id
    product = query(website_name, product_id)

    #check if the product is in database or not
    if product == None:
        return ('absent', None)

    #check if the product is valid or outdated
    current_datetime = datetime.now()
    valid_modified_on = current_datetime - timedelta(days=LIFESPAN)

    if valid_modified_on <= product.modified_on:
        return ('present', product.sentiment)
    else:
        return ('outdated', None)

def update_handler(website_name, product_id, action, url,
			        sentiment_score, sentiment):
    """Handler function for update operation"""

    return update(website_name=website_name, product_id=product_id, url=url, 
                    sentiment_score=sentiment_score, sentiment=sentiment)

def insert_handler(website_name, product_id, action, url,
			        sentiment_score, sentiment):
    """Handler function for insert operation"""

    return insert(website_name=website_name, product_id=product_id, url=url, 
                    sentiment_score=sentiment_score, sentiment=sentiment)

def driver(website_name, product_id, action, url=None,
            sentiment_score=None, sentiment=None):
    """Manages all the work related to database"""

    action = action.lower()
    if action == 'query':
        return query_handler(website_name, product_id)

    elif action == 'update':
	    return update_handler(website_name, product_id, action, url,
		                        sentiment_score, sentiment)

    elif action == 'insert':
	    return insert_handler(website_name, product_id, action, url,
		                    	sentiment_score, sentiment)

import dbsettings
from session import make_session
from sqlalchemy.orm import query
from datetime import datetime, timedelta

def query(website_name, product_id):
    """Returns the object which represents the row in database table
        with the given product id in the given website
    """

    return session.query(website_name).filter(website_name.product_id == product_id).one()

def update(website_name, product_id, url, sentiment_score, sentiment):
    """Update a product and it's sentiments in database
        after the lifespan of the sentiment has expired
    """

    #initiate a session
    session = make_session()

    #get the object
    product = query(website_name, product_id)

    #update the object
    product.url = url
    product.sentiment_score = sentiment_score
    product.sentiment = sentiment
    product.modified_on = datetime.now()

    try:
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()

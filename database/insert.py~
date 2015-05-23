from tables import AmazonIN, FlipkartCOM
from session import make_session
from datetime import datetime

def insert(website_name, product_id, url, sentiment_score, sentiment):
    """Inserts a product in the database"""

    #initiate a session
    session = make_session()

    #the date when the product is first analyzed
    date = datetime.now()

    if website_name == 'AmazonIN':
        #create the new product object of class AmazonIN
        new_product = AmazonIN(product_id=product_id, url=url, added_on=date, modified_on=date,
                                sentiment_score=sentiment_score, sentiment=sentiment)
    elif website_name == 'FlipkartCOM':
        new_product = FlipkartCOM(product_id=product_id, url=url, added_on=date, modified_on=date,
                                    sentiment_score=sentiment_score, sentiment=sentiment)

    try:
        session.add(new_product)
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()

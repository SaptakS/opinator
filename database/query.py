from sqlalchemy.orm import query

from session import make_session
from tables import AmazonIN, FlipkartCOM

def query(website_name, product_id):
    """Return the product object if the product is present
        in the database and None when not present
    """

    # initiate a new session
    session = make_session()

    # query for the product
    if website_name == 'AmazonIN':
        product = session.query(AmazonIN).filter(AmazonIN.product_id == product_id).first()
    elif website_name == 'FlipkartCOM':
        product = session.query(FlipkartCOM).filter(FlipkartCOM.product_id == product_id).first()

    # if the product is present in the database
    if product != None:
        product_modified_on = product.modified_on
        product_sentiment = product.sentiment

    try:
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()

    if product != None:
        return (product_modified_on, product_sentiment)
    else:
        return (None, None)

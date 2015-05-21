from session import make_session
from sqlalchemy.orm import query

def query(website_name, product_id):
    """Return the product object if the product is present
        in the database and None when not present
    """

    #initiate a new session
    session = make_session()

    #query for the product
    product = session.query(website_name).filter(website_name.product_id == product_id).first()

    try:
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()

    #Checking for the case when product is not there in the database
    if product != None:
        return product
    else:
        return None

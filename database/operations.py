from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tables import AmazonIN, FlipkartCOM
from tables import db_connect
from dbsettings import DBCONFIG, LIFESPAN

class Operations():
    """Does all the basic operations related to the database"""

    def __init__(self, website_name, product_id, url=None,
                    sentiment_score=None, sentiment=None):
        """Initialize the variables from the data received by the dbdriver"""

        self.website_name = website_name
        self.product_id = product_id
        self.url = url
        self.sentiment_score = sentiment_score
        self.sentiment = sentiment
        self.session = self.start_session()

    def start_session(self):
        """Starts a sqlalchemy session"""

        engine = db_connect()
        DBSession = sessionmaker(bind=engine)
        return DBSession()

    def end_session(self):
        """Ends a sqlalchemy session"""

        try:
            self.session.commit()
        except:
            self.session.rollback()
        finally:
            self.session.close()

    def insert(self):
        """Inserts a product in the database"""

        # the date when the product is first analyzed
        date = datetime.now()

        if self.website_name == 'AmazonIN':

            # create the new product object of class AmazonIN
            new_product = AmazonIN(product_id=self.product_id, url=self.url, added_on=date, modified_on=date,
                                    sentiment_score=self.sentiment_score, sentiment=self.sentiment)

        elif self.website_name == 'FlipkartCOM':

            # create the new product object of class FlipkartCOM
            new_product = FlipkartCOM(product_id=self.product_id, url=self.url, added_on=date, modified_on=date,
                                        sentiment_score=self.sentiment_score, sentiment=self.sentiment)

        # add the product to the database and end the session
        self.session.add(new_product)
        self.end_session()

    def query_update(self):
        """Returns the object which represents the row in database table
            with the given product id in the given website
            Helper function for update method
        """

        if self.website_name == 'AmazonIN':
            return self.session.query(AmazonIN).filter(AmazonIN.product_id == self.product_id).first()
        elif self.website_name == 'FlipkartCOM':
            return self.session.query(FlipkartCOM).filter(FlipkartCOM.product_id == self.product_id).first()

    def update(self):
        """Update a product and it's sentiments in database
            after the lifespan of the sentiment has expired
        """

        # get the object which has to be updated
        product = self.query_update()

        # update the object
        product.url = self.url
        product.sentiment_score = self.sentiment_score
        product.sentiment = self.sentiment
        product.modified_on = datetime.now()

        # end the session
        self.end_session()

    def query(self):
        """Return the product object if the product is present
            in the database and None when not present
        """

        # query for the product
        if self.website_name == 'AmazonIN':
            product = self.session.query(AmazonIN).filter(AmazonIN.product_id == self.product_id).first()
        elif self.website_name == 'FlipkartCOM':
            product = self.session.query(FlipkarCOM).filter(FlipkartCOM.product_id == self.product_id).first()

        # check if the query result doesn't return any product object,
        # otherwise access the dates
        if product != None:
            product_modified_on = product.modified_on
            product_sentiment = product.sentiment

        # end the session
        self.end_session()

        # return the dates if the product is present otherwise return none
        if product != None:
            return (product_modified_on, product_sentiment)
        else:
            return (None, None)

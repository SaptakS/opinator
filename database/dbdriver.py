from datetime import datetime, timedelta

from operations import Operations
from dbsettings import LIFESPAN

class Driver():
    """Drives the database"""

    def __init__(self, action, website_name, product_id,
                    url=None, sentiment_score=None, sentiment=None):
        """Initialize the variables with data from backend driver"""

        self.action = action.lower()
        self.website_name = website_name
        self.product_id = product_id
        self.url = url
        self.sentiment_score = sentiment_score
        self.sentiment = sentiment

    def query_handler(self, operation):
        """Handler function for query before scraping"""

        # query for given website_name and product_id
        product_modified_on, product_sentiment = operation.query()

        # check if the product is in database or not
        if product_modified_on == None:
            return ('absent', None)

        # check if the product is valid or outdated
        current_datetime = datetime.now()
        valid_modified_on = current_datetime - timedelta(days=LIFESPAN)

        if valid_modified_on <= product_modified_on:
            return ('present', product_sentiment)
        else:
            return ('outdated', None)

    def update_handler(self, operation):
        """Handler function for update operation"""

        return operation.update()

    def insert_handler(self, operation):
        """Handler function for insert operation"""

        return operation.insert()

    def drive(self):
        """Main method to drive the database"""

        if self.action == 'query':

            # create an operation object
            operation = Operations(website_name=self.website_name, product_id=self.product_id)
            return self.query_handler(operation)

        elif self.action == 'update':

            # create an operation object
            operation = Operations(website_name=self.website_name, product_id=self.product_id, url=self.url,
                                            sentiment_score=self.sentiment_score, sentiment=self.sentiment)
            return self.update_handler(operation)

        elif self.action == 'insert':

            # create an operation object
            operation = Operations(website_name=self.website_name, product_id=self.product_id, url=self.url,
                                        sentiment_score=self.sentiment_score, sentiment=self.sentiment)
            return self.insert_handler(operation)

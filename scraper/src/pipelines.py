import json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from op_tables import Reviews, Product, Sentiment
from op_tables import db_connect, create_tables

class OpinatorscraperPipeline(object):
    """Opinatorscraper pipeline for storing scraped items in the database"""

    def __init__(self):
        engine = db_connect()
        create_tables (engine)
        self.Session = sessionmaker(bind = engine)

    def process_item(self, item, spider):
        session = self.Session()
        reviews = item['reviews']

        new_list = []
        for i in reviews:
            new_list.append(i.encode('utf-8'))
        json_array_of_reviews = json.dumps(new_list)

        product_id = item['product_id']
        website_name = item['website_name']

        obj_Product = Product (product_id = product_id, website_name = website_name)
        obj_Product.reviews.append(Reviews (reviews = json_array_of_reviews))
        obj_Product.sentiment = Sentiment (dateTime = datetime.now())

        try:
            session.add(obj_Product)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item

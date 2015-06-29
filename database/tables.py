from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Numeric

from dbsettings import DBCONFIG

Base = declarative_base()

class AmazonIN (Base):
    """Table to store all products from amazon.in"""

    __tablename__ = 'amazon_in'

    product_id = Column(String(20), primary_key=True)
    url = Column (String(250), nullable=False)
    sentiment_score = Column (Numeric(3, 2))
    sentiment = Column (String(8), nullable=False)
    added_on = Column (DateTime, nullable=False)
    modified_on = Column (DateTime, nullable=False)


class FlipkartCOM(Base):
    """Table to store all products from flipkart.com"""

    __tablename__ = 'flipkart_com'

    product_id = Column(String(20), primary_key=True)
    url = Column (String(250), nullable=False)
    sentiment_score = Column (Numeric(precision=3))
    sentiment = Column (String(8), nullable=False)
    added_on = Column (DateTime, nullable=False)
    modified_on = Column (DateTime, nullable=False)

def db_connect():
    """Connects to the database using database configuration
        specified in dbsettings.py
    """

    return create_engine(URL(**DBCONFIG))

def create_tables(engine):
    """Creates the tables"""

    Base.metadata.create_all(engine)

engine = db_connect()
create_tables(engine)

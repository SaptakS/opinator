import settings
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.engine.url import URL

Base = declarative_base()

class Product (Base):
    __tablename__ = 'product'

    id = Column (Integer, primary_key = True)
    product_id = Column (String(250), nullable = False)
    website_name = Column (String(250), nullable = False)
    
    sentiment_id = Column (Integer, ForeignKey('sentiment.id'))    
    sentiment = relationship ("Sentiment", uselist = False)

class Reviews (Base):
    __tablename__ = 'review'

    id = Column (Integer, primary_key = True)
    product_id = Column (Integer, ForeignKey('product.id'))
    sentiment_id = Column (Integer, ForeignKey ('sentiment.id'))
    reviews = Column (Text(4294967295))

    product = relationship ("Product", backref = "reviews")
    sentiment = relationship ("Sentiment")

class Sentiment(Base):
    __tablename__ = 'sentiment'

    id = Column (Integer, primary_key = True)
    sentiment = Column (Text())
    dateTime = Column (DateTime, nullable = False)

def db_connect ():
    return create_engine(URL(**settings.DATABASE))

def create_tables (engine):
    Base.metadata.create_all (engine)

engine = db_connect ()
create_tables (engine)

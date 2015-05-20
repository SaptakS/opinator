import settings
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Numeric
from sqlalchemy.engine.url import URL

Base = declarative_base()

class mainTable(Base):
    __tablename__ = 'mainTable'

    id = Column (Integer, primary_key = True)
    productID = Column (String(20))
    website = Column (String(20))
    sentiment = Column (Integer)
    date = Column (DateTime)

def db_connect ():
    return create_engine(URL(**settings.DATABASE))

def create_tables (engine):
    Base.metadata.create_all (engine)

engine = db_connect ()
create_tables (engine)

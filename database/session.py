from tables import db_connect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

def make_session():
    """To make a sqlalchemy session"""
    
    engine = db_connect()
    DBSession = sessionmaker(bind=engine)
    return DBSession()

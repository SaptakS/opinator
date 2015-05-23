from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from tables import db_connect

def make_session():
    """Makes a sqlalchemy session"""

    engine = db_connect()
    DBSession = sessionmaker(bind=engine)
    return DBSession()

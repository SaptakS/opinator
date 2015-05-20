import json
from sys import arg
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tables import mainTable
from tables import db_connect, create_tables


engine = db_connect()
create_tables (engine)
session = sessionmaker(bind = engine)
sentiment = argv[1]
productID = argv[2]
obj = mainTable (sentiment = sentiment, productID = productID, date = datetime.now())
try:
    session.add(obj)        
    session.commit()
except:
    session.rollback()        
    raise
finally:
    session.close())

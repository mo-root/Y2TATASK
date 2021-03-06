from model import *
#import sqlite
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
#from IPython.core import get_ipython

# hist = get_ipython().history_manager
# hist.db = sqlite3.connect(hist.hist_file , check_same_thread = False)



engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
# session = scoped_session(sessionmaker(bind=engine))
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_item(name,email,comment,date,link):
	item_obj = Item(
		name=name,
		email=email,
		comment=comment,
		date=date,
		link=link)
		
	session.add(item_obj)
	session.commit()

def query_all():
	Items = session.query(Item).all()
	return Items


def delete1():
        Items = session.query(Item).all()
        session.Item.query.delete()
        session.commit()

def clear_data(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table %s' % table)
        session.execute(table.delete())
    session.commit()
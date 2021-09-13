from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()
class Item(Base):
	__tablename__ ="items"
	id = Column(Integer,primary_key=True)
	name = Column(String)
	email = Column(String)
	comment = Column(String)
	date = Column(String)
	link = Column(String)
	def __repr__(self):
		return("item: {}\n"
				"name: {}\n"
				"email : {}\n"
				"comment : {}\n"
				"date : {}\n"
				"link : {}\n").format(
				self.name,
				self.email,
				self.coment,
				self.date,
				self.link)
			

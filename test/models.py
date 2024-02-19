# from local
from database import Base
# from 3rd party lib
from sqlalchemy import Column, Integer, String


class Users(Base):
	__tablename__ = 'users'
	
	id = Column(Integer, primary_key=True, index=True)
	first_name = Column(String(50))
	last_name = Column(String(50))
	company_name = Column(String(50))
	age = Column(Integer)
	city = Column(String(50))
	state = Column(String(50))
	zip = Column(Integer)
	email = Column(String, unique=True, index=True)
	web = Column(String(50))

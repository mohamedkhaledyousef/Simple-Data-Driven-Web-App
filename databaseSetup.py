import os

#configration but at the begining of file
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#class definiation
class  Restaurant(Base):
	#table information
	__tablename__ = 'restaurant'

	#Mappers 
	id = Column(Integer,primary_key=True)
	name = Column(String(80),nullable=False)

#class definiation
class MenuItem(Base):		
	#table information
	__tablename__ = 'menu_item'

	#Mappers 
	name = Column(String(80),nullable=False)
	id = Column(Integer,primary_key=True)
	description=Column(String(250))
	price=Column(String(250))
	course=Column(String(250))
	restaurant_id =Column(Integer,ForeignKey('restaurant.id'))
	restaurant=relationship(Restaurant)

#class definiation
class  Employee(Base):
	#table information
	__tablename__ = 'employee'

	#Mappers 
	name = Column(String(80),nullable=False)
	id = Column(Integer,primary_key=True)
	

#class definiation
class  Address(Base):
	#table information
	__tablename__ = 'address'

	#Mappers 
	street = Column(String(80),nullable=False)	
	zib = Column(String(5),nullable=False)	
	id = Column(Integer,primary_key=True)
	employee_id = Column(Integer,ForeignKey('employee.id'))
	employee = relationship(Employee)

############configration but at the end of file ######

engine = create_engine(
'sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)


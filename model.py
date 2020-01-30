from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Animal(Base):
	__tablename__ = 'animal'
	id = Column(Integer, primary_key= True)
	name = Column(String)
	quantity_left = Column(Integer)
	locations = Column(String)
	description = Column(String)
	donations = Column(Integer)
	# def __init__ (self,donations):
	# 	self.donations= donations
	# def set_donation(self,donar):
	# 	self.donations+= donar.get_amount()
		

class Donars(Base):
	__tablename__ = 'donars'
	id = Column(Integer, primary_key= True)
	email = Column(String)
	amount = Column(Integer)
	animal_name = Column(String)
	note= Column(String)

	# def __init__ (self, animal, amount):
	# 	self.animal= animal
	# 	self.amount= amount
	# def get_amount(self):
	# 	return self.amount


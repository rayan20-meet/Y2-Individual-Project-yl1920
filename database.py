from model import *
from sqlalchemy.pool import SingletonThreadPool

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlite3

conn = sqlite3.connect('databases.py')

engine = create_engine('sqlite:///database.db',poolclass=SingletonThreadPool, connect_args={'check_same_thread':False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_animal(name,quantity_left,locations,description):

	Animal_object = Animal(
		name=name,
		quantity_left=quantity_left,
		locations=locations,
		description=description)
	session.add(Animal_object)
	session.commit()

def update_animal(name,quantity_left,locations,description,id):

	Animal = session.query(Animal).filter_by(id=id).first()
	Animal.name=name
	Animal.quantity_left=quantity_left
	Animal.locations=locations
	Animal.description=description
	Animal.id=id

	session.commit()

def remove_Animal(their_id):

	session.query(Animal).filter_by(id=their_id).delete()
	session.commit()


def query_all():
	animals=session.query(Animal).all()
	return animals
	

def specific_animal(name):
	return session.query(Animal).filter_by(name=name).one()


def query_all_donars():

	return session.query(Donars).all()

def Add_To_Donations(amount,animal):
	specific_animal(animal).donations+= amount
	session.commit()





	 
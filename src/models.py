import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    def serialize(self):
        return{
            "user_name":self.user_name,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "email":self.email,
        }

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=True)
    orbital_period = Column(String(250), nullable=True)
    diameter = Column(String(250), nullable=True)
  
    def serialize(self):
        return{
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter
        }

class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=True)
    manufacturer = Column(String(250), nullable=True)
    cargo_capacity= Column(String(250), nullable=True)
  
    def serialize(self):
        return{
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cargo_capacity": self.cargo_capacity
        }
class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=True)
    skin_color = Column(String(250), nullable=True)
    birth_year= Column(String(250), nullable=True)
  
    def serialize(self):
        return{
            "eye_color": self.eye_color,
            "skin_color": self.skin_color,
            "birth_year": self.birth_year
        }
    
class Fav(Base):
    __tablename__ = 'fav'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'),nullable=False)
    people_id = Column(Integer,ForeignKey('people.id'),nullable=True)
    planets_id = Column(Integer,ForeignKey('planets.id'),nullable=True)
    starships_id = Column(Integer,ForeignKey('starships.id'),nullable=True)

    user = relationship(User)
    people = relationship(People)
    planets = relationship(Planets)
    starships = relationship(Starships)
  
  
    def serialize(self):
        return{
            "user_id":self.user_id,
            "people_id":self.people_id,
            "planets_id":self.planets_id,
            "starships_id":self.starships_id

        }
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

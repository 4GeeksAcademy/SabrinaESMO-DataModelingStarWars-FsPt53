import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User (Base):
    __tablename__='User'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), index=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    email = Column(String(40), nullable=False)
    fav_planet_id = Column(Integer)
    fav_film_id = Column(Integer)

class Planets (Base):
    __tablename__='Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

class Films (Base):
    __tablename__='Films'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

class Vehicles (Base):
    __tablename__='Vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

class FavoritePlanets (Base):
    __tablename__='FavoritePlanets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    planets_id = Column(ForeignKey('Planets.id'))
    planets = relationship(Planets)

class FavoriteFilms (Base):
    __tablename__='FavoriteFilms'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    films_id = Column(ForeignKey('Films.id'))
    films = relationship(Films)

class FavoriteVehicles (Base):
    __tablename__='FavoriteVehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    vehicles_id = Column(ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

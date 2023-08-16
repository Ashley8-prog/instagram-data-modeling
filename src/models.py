import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
#Tabla que me conecta
class DatosInsta(Base):
    __tablename__ = 'datosinsta'
    id = Column(Integer, primary_key=True)
    perfil_id = Column(Integer, ForeignKey('perfil.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    postear_id = Column(Integer, ForeignKey('postear.id'))
    acciones_id = Column(Integer, ForeignKey('acciones.id'))

class Acciones(Base):
    __tablename__ = 'acciones' 
    id = Column(Integer, primary_key=True)
    comment = Column(String(500), nullable=True)
    mention = Column(String(200), nullable=True)
    save = Column(String(10), nullable=True)
    share = Column(String(10), nullable=True)
    

class Perfil(Base):
    __tablename__ = 'perfil'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(500), nullable = True)
    number_of_followers = Column(Integer, nullable = True)


class Postear(Base):
     __tablename__ = 'postear'
     id = Column(Integer, primary_key=True)
     edit_description = Column(String(400), nullable=False)
     autor_description = Column(String(100), nullable=False)
     mencionar_personas = Column(String(500), nullable=True)
     responder_comentario = Column(String(700), nullable=True)
    

class Usuario(Base):
    __tablename__ = 'usuario'
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(200), nullable=False)
    username = Column(String(100), nullable=False)
    # aqui relationship
    perfil = relationship(Perfil, backref='usuario',lazy=True)
    # datosinsta = relationship(DatosInsta, backref='usuario',lazy=True)
    postear = relationship(Postear, backref='usuario',lazy=True)
    acciones = relationship(Acciones, backref='usuario',lazy=True)






    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

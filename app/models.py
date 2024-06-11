from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Auto(Base):
    __tablename__ = 'autos'
    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String(250), index=True)
    modelo = Column(String(250), index=True)
    vendido = Column(Boolean, default=False)

class Venta(Base):
    __tablename__ = 'ventas'
    id = Column(Integer, primary_key=True, index=True)
    auto_id = Column(Integer, ForeignKey('autos.id'))
    auto = relationship("Auto")
    comprador = Column(String(250), index=True)
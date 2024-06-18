from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Session
from .database import Base

class Auto(Base):
    __tablename__ = 'autos'
    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String(250), index=True)
    modelo = Column(String(250), index=True)
    vendido = Column(Boolean, default=False)

    @classmethod
    def create(cls, session: Session, **kwargs):
        new_auto = cls(**kwargs)
        session.add(new_auto)
        session.commit()
        session.refresh(new_auto)
        return new_auto

    @classmethod
    def read(cls, session: Session, auto_id: int):
        return session.query(cls).filter(cls.id == auto_id).first()

    @classmethod
    def read_all(cls, session: Session, skip: int = 0, limit: int = 10):
        return session.query(cls).offset(skip).limit(limit).all()

    def update(self, session: Session, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        session.commit()
        session.refresh(self)
        return self

    def delete(self, session: Session):
        session.delete(self)
        session.commit()

class Venta(Base):
    __tablename__ = 'ventas'
    id = Column(Integer, primary_key=True, index=True)
    auto_id = Column(Integer, ForeignKey('autos.id'))
    auto = relationship("Auto")
    comprador = Column(String(250), index=True)

    @classmethod
    def create(cls, session: Session, **kwargs):
        new_venta = cls(**kwargs)
        session.add(new_venta)
        session.commit()
        session.refresh(new_venta)
        return new_venta

    @classmethod
    def read(cls, session: Session, venta_id: int):
        return session.query(cls).filter(cls.id == venta_id).first()

    @classmethod
    def read_all(cls, session: Session, skip: int = 0, limit: int = 10):
        return session.query(cls).offset(skip).limit(limit).all()

    def update(self, session: Session, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        session.commit()
        session.refresh(self)
        return self

    def delete(self, session: Session):
        session.delete(self)
        session.commit()
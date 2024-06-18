from sqlalchemy.orm import Session
from . import models, schemas

def create_auto(db: Session, auto: schemas.AutoCreate):
    return models.Auto.create(db, **auto.dict())

def get_auto(db: Session, auto_id: int):
    return models.Auto.read(db, auto_id)

def get_autos(db: Session, skip: int = 0, limit: int = 10):
    return models.Auto.read_all(db, skip, limit)

def update_auto(db: Session, auto_id: int, auto: schemas.AutoUpdate):
    db_auto = models.Auto.read(db, auto_id)
    if db_auto:
        return db_auto.update(db, **auto.dict())
    return None

def delete_auto(db: Session, auto_id: int):
    db_auto = models.Auto.read(db, auto_id)
    if db_auto:
        db_auto.delete(db)
    return db_auto
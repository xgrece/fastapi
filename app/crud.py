from sqlalchemy.orm import Session
from . import models, schemas

# Crear un auto
def create_auto(db: Session, auto: schemas.AutoCreate):
    db_auto = models.Auto(**auto.dict())
    db.add(db_auto)
    db.commit()
    db.refresh(db_auto)
    return db_auto

# Obtener un auto por ID
def get_auto(db: Session, auto_id: int):
    return db.query(models.Auto).filter(models.Auto.id == auto_id).first()

# Obtener todos los autos
def get_autos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Auto).offset(skip).limit(limit).all()

# Actualizar un auto
def update_auto(db: Session, auto_id: int, auto: schemas.AutoUpdate):
    db_auto = db.query(models.Auto).filter(models.Auto.id == auto_id).first()
    if db_auto is None:
        return None
    for key, value in auto.dict().items():
        setattr(db_auto, key, value)
    db.commit()
    db.refresh(db_auto)
    return db_auto

# Eliminar un auto
def delete_auto(db: Session, auto_id: int):
    db_auto = db.query(models.Auto).filter(models.Auto.id == auto_id).first()
    if db_auto:
        db.delete(db_auto)
        db.commit()
    return db_auto
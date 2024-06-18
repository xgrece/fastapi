from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear un auto
@router.post("/autos/", response_model=schemas.Auto)
def create_auto(auto: schemas.AutoCreate, db: Session = Depends(get_db)):
    return models.Auto.create(db, **auto.dict())

# Obtener todos los autos
@router.get("/autos/", response_model=list[schemas.Auto])
def read_autos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return models.Auto.read_all(db, skip=skip, limit=limit)

# Obtener un auto por ID
@router.get("/autos/{auto_id}", response_model=schemas.Auto)
def read_auto(auto_id: int, db: Session = Depends(get_db)):
    db_auto = models.Auto.read(db, auto_id)
    if db_auto is None:
        raise HTTPException(status_code=404, detail="Auto not found")
    return db_auto

# Actualizar un auto
@router.put("/autos/{auto_id}", response_model=schemas.Auto)
def update_auto(auto_id: int, auto: schemas.AutoUpdate, db: Session = Depends(get_db)):
    db_auto = models.Auto.read(db, auto_id)
    if db_auto is None:
        raise HTTPException(status_code=404, detail="Auto not found")
    return db_auto.update(db, **auto.dict())

# Eliminar un auto
@router.delete("/autos/{auto_id}", response_model=schemas.Auto)
def delete_auto(auto_id: int, db: Session = Depends(get_db)):
    db_auto = models.Auto.read(db, auto_id)
    if db_auto is None:
        raise HTTPException(status_code=404, detail="Auto not found")
    db_auto.delete(db)
    return db_auto
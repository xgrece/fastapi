from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
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
    return crud.create_auto(db=db, auto=auto)

# Obtener todos los autos
@router.get("/autos/", response_model=list[schemas.Auto])
def read_autos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    autos = crud.get_autos(db, skip=skip, limit=limit)
    return autos

# Obtener un auto por ID
@router.get("/autos/{auto_id}", response_model=schemas.Auto)
def read_auto(auto_id: int, db: Session = Depends(get_db)):
    db_auto = crud.get_auto(db, auto_id=auto_id)
    if db_auto is None:
        raise HTTPException(status_code=404, detail="Auto not found")
    return db_auto

# Actualizar un auto
@router.put("/autos/{auto_id}", response_model=schemas.Auto)
def update_auto(auto_id: int, auto: schemas.AutoUpdate, db: Session = Depends(get_db)):
    db_auto = crud.update_auto(db, auto_id=auto_id, auto=auto)
    if db_auto is None:
        raise HTTPException(status_code=404, detail="Auto not found")
    return db_auto

# Eliminar un auto
@router.delete("/autos/{auto_id}", response_model=schemas.Auto)
def delete_auto(auto_id: int, db: Session = Depends(get_db)):
    db_auto = crud.delete_auto(db, auto_id=auto_id)
    if db_auto is None:
        raise HTTPException(status_code=404, detail="Auto not found")
    return db_auto
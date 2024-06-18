from fastapi import FastAPI, Request, Form, Depends, HTTPException
from .database import engine, Base
from .models import Auto, Venta
from .endpoints import autos
from . import models
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from sqlalchemy.orm import Session
from .database import engine, SessionLocal

#Iniciar el server: uvicorn main:app --reload
#uvicorn app.main:app --reload

# detener el server: CTRL+C
    
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configuración de Jinja2Templates para usar la carpeta 'templates'
templates = Jinja2Templates(directory="app/templates")

# Montar la carpeta static para servir archivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/create", response_class=HTMLResponse)
async def create_auto_form(request: Request):
    return templates.TemplateResponse("create_auto.html", {"request": request})

@app.post("/create", response_class=HTMLResponse)
async def create_auto(request: Request, marca: str = Form(...), modelo: str = Form(...), vendido: bool = Form(False), db: Session = Depends(get_db)):
    new_auto = Auto.create(db, marca=marca, modelo=modelo, vendido=vendido)
    return templates.TemplateResponse("create_auto.html", {"request": request, "message": "Auto creado con éxito"})

@app.get("/read", response_class=HTMLResponse)
async def read_autos(request: Request, db: Session = Depends(get_db)):
    autos = Auto.read_all(db)
    return templates.TemplateResponse("read_autos.html", {"request": request, "autos": autos})

@app.get("/update", response_class=HTMLResponse)
async def update_auto_form(request: Request):
    return templates.TemplateResponse("update_auto.html", {"request": request})

@app.post("/update", response_class=HTMLResponse)
async def update_auto(request: Request, id: int = Form(...), marca: str = Form(None), modelo: str = Form(None), vendido: bool = Form(None), db: Session = Depends(get_db)):
    auto = Auto.read(db, id)
    if auto:
        auto.update(db, marca=marca, modelo=modelo, vendido=vendido)
        return templates.TemplateResponse("update_auto.html", {"request": request, "message": "Auto actualizado con éxito"})
    else:
        raise HTTPException(status_code=404, detail="Auto no encontrado")

@app.get("/delete", response_class=HTMLResponse)
async def delete_auto_form(request: Request):
    return templates.TemplateResponse("delete_auto.html", {"request": request})

@app.post("/delete", response_class=HTMLResponse)
async def delete_auto(request: Request, id: int = Form(...), db: Session = Depends(get_db)):
    auto = Auto.read(db, id)
    if auto:
        auto.delete(db)
        return templates.TemplateResponse("delete_auto.html", {"request": request, "message": "Auto eliminado con éxito"})
    else:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
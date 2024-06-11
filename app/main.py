from fastapi import FastAPI
from .database import engine, Base
from .models import Auto, Venta
from .endpoints import autos

#Iniciar el server: uvicorn main:app --reload
# detener el server: CTRL+C
    
app = FastAPI()

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir el router de autos
app.include_router(autos.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Car Dealership API"}
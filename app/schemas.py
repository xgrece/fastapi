from pydantic import BaseModel

class AutoBase(BaseModel):
    marca: str
    modelo: str
    vendido: bool = False

class AutoCreate(AutoBase):
    pass

class AutoUpdate(AutoBase):
    pass

class Auto(AutoBase):
    id: int

    class Config:
        orm_mode = True
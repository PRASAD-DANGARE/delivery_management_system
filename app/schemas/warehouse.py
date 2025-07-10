from pydantic import BaseModel

class WarehouseBase(BaseModel):
    name: str
    latitude: float
    longitude: float

class WarehouseCreate(WarehouseBase):
    pass

class WarehouseOut(WarehouseBase):
    id: int
    class Config:
        orm_mode = True
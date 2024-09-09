from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    description: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

class ItemUpdate(BaseModel):
    name: str
    description: Optional[str] = None

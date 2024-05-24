from typing import List, Optional
from pydantic import BaseModel

class BranchBase(BaseModel):
    ifsc: str
    bank_id: int
    branch: str
    address: str
    city: str
    district: str
    state: str

class BranchCreate(BranchBase):
    pass

class Branch(BranchBase):
    class Config:
        orm_mode = True

class BankBase(BaseModel):
    name: str

class BankCreate(BankBase):
    pass

class Bank(BankBase):
    id: int
    branches: List[Branch] = []
    class Config:
        orm_mode = True

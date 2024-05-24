from fastapi import FastAPI, Depends, HTTPException,status
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from typing import List, Annotated
from models import Bank, Branch
from schema import BankCreate, BranchCreate, Bank as BankSchema, Branch as BranchSchema
from database import engine, get_db, Base
import uvicorn

app = FastAPI()
Base.metadata.create_all(bind=engine)
db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/", description="Hello World")
async def hello():
    return {"Hello": "World"}


@app.post("/create_bank/")
async def create_bank(bank: BankCreate, db: db_dependency):
    existing_bank = db.query(Bank).filter(Bank.name == bank.name).first()
    if existing_bank:
        raise HTTPException(status_code=409, detail="Bank with this name already exists")
    new_bank = Bank(name=bank.name)
    db.add(new_bank)
    db.commit()
    db.refresh(new_bank)
    return new_bank


@app.get("/read_banks/", status_code=status.HTTP_200_OK, response_model=List[BankSchema])
async def read_banks(db: Session = Depends(get_db)):
    banks = db.query(Bank).all()
    return banks


@app.post("/create_branch/",status_code=status.HTTP_201_CREATED,description="APIs for creating Branches for specific Branch")
async def create_branch(branch:BranchCreate , db:db_dependency):
   bank= db.get(Bank,branch.bank_id)
   if not bank:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Bank Not Found")
   new_branch=Branch(
       ifsc=branch.ifsc,
       bank_id=branch.bank_id,
       branch=branch.branch,
       address=branch.address,
       city=branch.city,
       district=branch.district,
       state=branch.state
   )
   db.add(new_branch)
   db.commit()
   db.refresh(new_branch)
   return new_branch

@app.get('/branch/{id}',response_model=BranchSchema,status_code=status.HTTP_200_OK)
async def branch(id:int,db:db_dependency):
    branch = db.query(Branch).filter(Branch.bank_id==id).first()
    if not branch:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Branches not found")
    
    return branch
    

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

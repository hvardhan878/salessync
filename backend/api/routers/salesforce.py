from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from .. import db

router = APIRouter(prefix="/salesforce", tags=["salesforce"])

class Account(BaseModel):
    id: str
    name: str
    industry: str

class Opportunity(BaseModel):
    id: str
    name: str
    stage: str
    amount: float

@router.get("/accounts", response_model=List[Account])
def get_accounts():
    return [Account(**dict(row)) for row in db.get_accounts()]

@router.post("/accounts", response_model=Account)
def create_account(account: Account):
    if any(a.id == account.id for a in get_accounts()):
        raise HTTPException(status_code=400, detail="Account ID already exists")
    db.create_account(account.id, account.name, account.industry)
    return account

@router.delete("/accounts/{account_id}")
def delete_account(account_id: str):
    deleted = db.delete_account(account_id)
    if deleted:
        return {"message": "Account deleted"}
    raise HTTPException(status_code=404, detail="Account not found")

@router.get("/opportunities", response_model=List[Opportunity])
def get_opportunities():
    return [Opportunity(**dict(row)) for row in db.get_opportunities()]

@router.post("/opportunities", response_model=Opportunity)
def create_opportunity(opportunity: Opportunity):
    if any(o.id == opportunity.id for o in get_opportunities()):
        raise HTTPException(status_code=400, detail="Opportunity ID already exists")
    db.create_opportunity(opportunity.id, opportunity.name, opportunity.stage, opportunity.amount)
    return opportunity

@router.delete("/opportunities/{opportunity_id}")
def delete_opportunity(opportunity_id: str):
    deleted = db.delete_opportunity(opportunity_id)
    if deleted:
        return {"message": "Opportunity deleted"}
    raise HTTPException(status_code=404, detail="Opportunity not found")
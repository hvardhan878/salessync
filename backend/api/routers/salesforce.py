from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

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
    # Mock Salesforce accounts
    return [
        Account(id="001", name="Acme Corp", industry="Manufacturing"),
        Account(id="002", name="Globex Inc", industry="Technology"),
    ]

@router.get("/opportunities", response_model=List[Opportunity])
def get_opportunities():
    # Mock Salesforce opportunities
    return [
        Opportunity(id="op1", name="Big Deal", stage="Prospecting", amount=100000.0),
        Opportunity(id="op2", name="Renewal", stage="Closed Won", amount=50000.0),
    ]
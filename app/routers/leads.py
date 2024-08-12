from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/leads/", response_model=schemas.Lead, operation_id="create_new_lead")
def create_lead(lead: schemas.LeadCreate, db: Session = Depends(get_db)):
    db_lead = crud.get_lead_by_email(db, email=lead.email)
    if db_lead:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_lead(db=db, lead=lead)

@router.get("/leads/", response_model=List[schemas.Lead], operation_id="get_all_leads")
def read_leads(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    leads = crud.get_leads(db, skip=skip, limit=limit)
    return leads

@router.get("/leads/{lead_id}", response_model=schemas.Lead, operation_id="get_lead_by_id")
def read_lead(lead_id: int, db: Session = Depends(get_db)):
    db_lead = crud.get_lead(db, lead_id=lead_id)
    if db_lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    return db_lead

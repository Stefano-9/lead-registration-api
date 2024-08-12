from sqlalchemy.orm import Session
from app import models, schemas

def get_lead(db: Session, lead_id: int):
    return db.query(models.Lead).filter(models.Lead.id == lead_id).first()

def get_leads(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Lead).offset(skip).limit(limit).all()

def get_lead_by_email(db: Session, email: str):
    return db.query(models.Lead).filter(models.Lead.email == email).first()

def create_lead(db: Session, lead: schemas.LeadCreate):
    db_lead = models.Lead(
        full_name=lead.full_name,
        email=lead.email,
        address=lead.address,
        phone_number=lead.phone_number  
    )
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    
    for course in lead.courses:
        db_course = models.Course(
            name=course.name,
            duration=course.duration,
            year=course.year,  
            lead_id=db_lead.id
        )
        db.add(db_course)
    db.commit()
    db.refresh(db_lead)
    return db_lead

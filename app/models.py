from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    address = Column(String)
    phone_number = Column(String)  
    registration_year = Column(Integer)  
    courses = relationship("Course", back_populates="owner")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    duration = Column(Integer)  
    year = Column(Integer)  
    lead_id = Column(Integer, ForeignKey("leads.id"))
    owner = relationship("Lead", back_populates="courses")

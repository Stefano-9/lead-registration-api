from typing import List
from pydantic import BaseModel

class CourseBase(BaseModel):
    name: str
    duration: int
    year: int

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int

    class Config:
        from_attributes = True  

class LeadBase(BaseModel):
    full_name: str
    email: str
    address: str
    phone_number: str
    courses: List[CourseCreate] = []

class LeadCreate(LeadBase):
    pass

class Lead(LeadBase):
    id: int
    courses: List[Course] = []

    class Config:
        from_attributes = True  

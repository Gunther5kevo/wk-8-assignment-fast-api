from pydantic import BaseModel, Field
from typing import List, Optional
import datetime

# Appointment Schemas
class AppointmentBase(BaseModel):
    description: str
    date: Optional[datetime.datetime] = None

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int
    patient_id: int

    class Config:
        orm_mode = True

# Patient Schemas
class PatientBase(BaseModel):
    name: str
    age: int
    gender: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    appointments: List[Appointment] = Field(default_factory=list)

    class Config:
        orm_mode = True

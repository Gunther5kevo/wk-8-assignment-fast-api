from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("/patients/{patient_id}", response_model=schemas.Appointment)
def create_appointment(patient_id: int, appointment: schemas.AppointmentCreate, db: Session = Depends(database.get_db)):
    patient = crud.get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return crud.create_appointment(db, appointment, patient_id)

@router.get("/", response_model=list[schemas.Appointment])
def read_appointments(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_appointments(db, skip=skip, limit=limit)

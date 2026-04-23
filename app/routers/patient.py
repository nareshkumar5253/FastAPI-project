from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate
from app.dependencies import get_db

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post("/")
def create_patient(data: PatientCreate, db: Session = Depends(get_db)):
    patient = Patient(**data.dict())
    db.add(patient)
    db.commit()
    return patient

@router.get("/search")
def search(name: str = None, phone: str = None, db: Session = Depends(get_db)):
    query = db.query(Patient)
    if name:
        query = query.filter(Patient.name.contains(name))
    if phone:
        query = query.filter(Patient.phone.contains(phone))
    return query.all()
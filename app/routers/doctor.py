from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate
from app.dependencies import get_db

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.post("/")
def create_doctor(data: DoctorCreate, db: Session = Depends(get_db)):
    doctor = Doctor(**data.dict())
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor

@router.get("/")
def get_doctors(specialization: str = None, db: Session = Depends(get_db)):
    query = db.query(Doctor)
    if specialization:
        query = query.filter(Doctor.specialization == specialization)
    return query.all()

@router.put("/{id}")
def update_doctor(id: int, data: DoctorCreate, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).get(id)
    if not doctor:
        raise HTTPException(404)
    for key, value in data.dict().items():
        setattr(doctor, key, value)
    db.commit()
    return doctor

@router.delete("/{id}")
def delete_doctor(id: int, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).get(id)
    if not doctor:
        raise HTTPException(404)
    db.delete(doctor)
    db.commit()
    return {"msg": "Deleted"}

@router.patch("/{id}/status")
def toggle_status(id: int, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).get(id)
    doctor.is_active = not doctor.is_active
    db.commit()
    return doctor
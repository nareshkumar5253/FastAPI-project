from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate
from app.dependencies import get_db

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("/")
def create(data: AppointmentCreate, db: Session = Depends(get_db)):
    appt = Appointment(**data.dict())
    db.add(appt)
    db.commit()
    return appt

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return db.query(Appointment).all()

@router.patch("/{id}/cancel")
def cancel(id: int, db: Session = Depends(get_db)):
    appt = db.query(Appointment).get(id)
    appt.status = "Cancelled"
    db.commit()
    return appt
from pydantic import BaseModel

class PatientCreate(BaseModel):
    name: str
    phone: str

class PatientOut(PatientCreate):
    id: int

    class Config:
        from_attributes = True
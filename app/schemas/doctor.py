from pydantic import BaseModel

class DoctorCreate(BaseModel):
    name: str
    specialization: str

class DoctorOut(DoctorCreate):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
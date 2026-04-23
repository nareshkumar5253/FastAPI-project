from fastapi import APIRouter
from app.schemas.auth import LoginRequest
from app.core.security import create_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(data: LoginRequest):
    if data.username == "admin" and data.password == "admin":
        token = create_token({"sub": data.username})
        return {"access_token": token}
    return {"error": "Invalid credentials"}
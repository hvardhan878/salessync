from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from .. import db

router = APIRouter(prefix="/auth", tags=["auth"])

class LoginRequest(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    username: str
    full_name: str

class RegisterRequest(BaseModel):
    username: str
    password: str
    full_name: str

@router.post("/login", response_model=UserResponse)
def login(data: LoginRequest):
    user = db.get_user_by_username(data.username)
    if user and user["password"] == data.password:
        return UserResponse(username=user["username"], full_name=user["full_name"])
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

@router.post("/logout")
def logout():
    return {"message": "Logged out (mock)"}

@router.get("/me", response_model=UserResponse)
def get_current_user():
    # For demo, always returns the demo user
    user = db.get_user_by_username("demo")
    return UserResponse(username=user["username"], full_name=user["full_name"])

@router.post("/register", response_model=UserResponse)
def register(data: RegisterRequest):
    if db.get_user_by_username(data.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    db.create_user(data.username, data.password, data.full_name)
    return UserResponse(username=data.username, full_name=data.full_name)
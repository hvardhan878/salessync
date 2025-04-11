from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["auth"])

# Mock user database
MOCK_USER = {"username": "demo", "password": "password", "full_name": "Demo User"}

class LoginRequest(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    username: str
    full_name: str

@router.post("/login", response_model=UserResponse)
def login(data: LoginRequest):
    if data.username == MOCK_USER["username"] and data.password == MOCK_USER["password"]:
        return UserResponse(username=MOCK_USER["username"], full_name=MOCK_USER["full_name"])
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

@router.post("/logout")
def logout():
    return {"message": "Logged out (mock)"}

@router.get("/me", response_model=UserResponse)
def get_current_user():
    # Always returns the mock user
    return UserResponse(username=MOCK_USER["username"], full_name=MOCK_USER["full_name"])
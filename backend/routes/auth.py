from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from services.supabase_service import SupabaseService
from utils.auth import create_access_token
from typing import Dict, Any

router = APIRouter(prefix="/auth", tags=["auth"])

class SignUpRequest(BaseModel):
    email: EmailStr
    password: str

class SignInRequest(BaseModel):
    email: EmailStr
    password: str

class AuthResponse(BaseModel):
    access_token: str
    user: Dict[str, Any]

@router.post("/signup", response_model=AuthResponse)
async def sign_up(request: SignUpRequest):
    try:
        supabase = SupabaseService()
        response = await supabase.sign_up(request.email, request.password)
        
        # Crea token JWT
        access_token = create_access_token(
            data={"sub": response.user.id},
            expires_delta=None
        )
        
        return AuthResponse(
            access_token=access_token,
            user=response.user
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/signin", response_model=AuthResponse)
async def sign_in(request: SignInRequest):
    try:
        supabase = SupabaseService()
        response = await supabase.sign_in(request.email, request.password)
        
        # Crea token JWT
        access_token = create_access_token(
            data={"sub": response.user.id},
            expires_delta=None
        )
        
        return AuthResponse(
            access_token=access_token,
            user=response.user
        )
        
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e)) 
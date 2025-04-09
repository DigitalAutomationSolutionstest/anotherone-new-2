from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from services.ai_service import AIService
from utils.auth import get_current_user

router = APIRouter(prefix="/chat", tags=["chat"])

class ChatRequest(BaseModel):
    message: str
    model: str = "claude"  # "claude" o "mistral"
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1000

class ChatResponse(BaseModel):
    response: str
    model: str
    tokens_used: int

@router.post("/send", response_model=ChatResponse)
async def send_message(
    request: ChatRequest,
    current_user = Depends(get_current_user)
):
    try:
        ai_service = AIService()
        
        if request.model == "claude":
            response = await ai_service.get_claude_response(
                request.message,
                temperature=request.temperature,
                max_tokens=request.max_tokens
            )
        else:
            response = await ai_service.get_mistral_response(
                request.message,
                temperature=request.temperature,
                max_tokens=request.max_tokens
            )
            
        return ChatResponse(
            response=response["text"],
            model=request.model,
            tokens_used=response["tokens_used"]
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
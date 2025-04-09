from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from services.stripe_service import StripeService
from utils.auth import get_current_user
from typing import Dict, Any

router = APIRouter(prefix="/payments", tags=["payments"])

class CheckoutRequest(BaseModel):
    price_id: str

class PaymentResponse(BaseModel):
    url: str
    session_id: str

@router.post("/create-checkout-session", response_model=PaymentResponse)
async def create_checkout_session(
    request: CheckoutRequest,
    current_user: Dict[str, Any] = Depends(get_current_user)
):
    try:
        stripe_service = StripeService()
        session = await stripe_service.create_checkout_session(
            price_id=request.price_id,
            user_id=current_user["id"]
        )
        return PaymentResponse(
            url=session.url,
            session_id=session.id
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/create-portal-session")
async def create_portal_session(
    current_user: Dict[str, Any] = Depends(get_current_user)
):
    try:
        stripe_service = StripeService()
        session = await stripe_service.create_portal_session(
            customer_id=current_user["stripe_customer_id"]
        )
        return {"url": session.url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/subscription/{subscription_id}")
async def get_subscription(
    subscription_id: str,
    current_user: Dict[str, Any] = Depends(get_current_user)
):
    try:
        stripe_service = StripeService()
        subscription = await stripe_service.get_subscription(subscription_id)
        return subscription
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/subscription/{subscription_id}")
async def cancel_subscription(
    subscription_id: str,
    current_user: Dict[str, Any] = Depends(get_current_user)
):
    try:
        stripe_service = StripeService()
        subscription = await stripe_service.cancel_subscription(subscription_id)
        return subscription
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 
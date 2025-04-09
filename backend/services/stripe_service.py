import stripe
from config.config import settings
from typing import Dict, Any, Optional

class StripeService:
    def __init__(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
    async def create_checkout_session(self, price_id: str, user_id: str) -> Dict[str, Any]:
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': price_id,
                    'quantity': 1,
                }],
                mode='subscription',
                success_url='http://localhost:3000/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url='http://localhost:3000/cancel',
                client_reference_id=user_id,
            )
            return session
        except Exception as e:
            raise Exception(f"Errore nella creazione della sessione di checkout: {str(e)}")
            
    async def create_portal_session(self, customer_id: str) -> Dict[str, Any]:
        try:
            session = stripe.billing_portal.Session.create(
                customer=customer_id,
                return_url='http://localhost:3000/account',
            )
            return session
        except Exception as e:
            raise Exception(f"Errore nella creazione della sessione del portale: {str(e)}")
            
    async def get_subscription(self, subscription_id: str) -> Optional[Dict[str, Any]]:
        try:
            subscription = stripe.Subscription.retrieve(subscription_id)
            return subscription
        except Exception as e:
            raise Exception(f"Errore nel recupero dell'abbonamento: {str(e)}")
            
    async def cancel_subscription(self, subscription_id: str) -> Dict[str, Any]:
        try:
            subscription = stripe.Subscription.delete(subscription_id)
            return subscription
        except Exception as e:
            raise Exception(f"Errore nella cancellazione dell'abbonamento: {str(e)}")
            
    async def create_customer(self, email: str, user_id: str) -> Dict[str, Any]:
        try:
            customer = stripe.Customer.create(
                email=email,
                metadata={
                    'user_id': user_id
                }
            )
            return customer
        except Exception as e:
            raise Exception(f"Errore nella creazione del cliente: {str(e)}") 
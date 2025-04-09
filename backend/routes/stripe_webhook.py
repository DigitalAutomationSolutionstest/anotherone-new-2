from fastapi import APIRouter, Request, Header, HTTPException
import stripe
import os
from supabase import create_client
from typing import Dict, Any

router = APIRouter()

# Configurazione Stripe
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

# Configurazione Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@router.post("/webhook")
async def stripe_webhook(request: Request, stripe_signature: str = Header(None)):
    try:
        # Ottieni il payload del webhook
        payload = await request.body()
        
        # Verifica la firma del webhook
        try:
            event = stripe.Webhook.construct_event(
                payload, stripe_signature, endpoint_secret
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Errore nella verifica della firma: {str(e)}")

        # Gestisci gli eventi
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            customer_email = session['customer_email']
            
            # Aggiorna il ruolo dell'utente in Supabase
            try:
                supabase.table("users").update({"role": "pro"}).eq("email", customer_email).execute()
                print(f"Utente {customer_email} aggiornato a pro")
            except Exception as e:
                print(f"Errore nell'aggiornamento dell'utente: {str(e)}")
                raise HTTPException(status_code=500, detail="Errore nell'aggiornamento dell'utente")

        elif event['type'] == 'customer.subscription.deleted':
            subscription = event['data']['object']
            customer_email = subscription['customer_email']
            
            # Rimuovi il ruolo pro dall'utente
            try:
                supabase.table("users").update({"role": "free"}).eq("email", customer_email).execute()
                print(f"Utente {customer_email} tornato a free")
            except Exception as e:
                print(f"Errore nell'aggiornamento dell'utente: {str(e)}")
                raise HTTPException(status_code=500, detail="Errore nell'aggiornamento dell'utente")

        return {"status": "success"}

    except Exception as e:
        print(f"Errore generale nel webhook: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) 
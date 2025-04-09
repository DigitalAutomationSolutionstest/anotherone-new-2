import stripe
import os
from dotenv import load_dotenv

load_dotenv()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

# Piani da creare
plans = [
    {
        "name": "Free Plan",
        "description": "Accesso gratuito limitato",
        "price": 0,
        "interval": "month",
    },
    {
        "name": "Pro Plan",
        "description": "Accesso illimitato alle mini-app AI",
        "price": 999,  # in centesimi: €9.99
        "interval": "month",
    },
    {
        "name": "Team Plan",
        "description": "Fino a 3 utenti + esportazione dati",
        "price": 2900,  # €29.00
        "interval": "month",
    }
]

created = []

for plan in plans:
    product = stripe.Product.create(
        name=plan["name"],
        description=plan["description"]
    )
    price = stripe.Price.create(
        unit_amount=plan["price"],
        currency="eur",
        recurring={"interval": plan["interval"]},
        product=product.id,
    )
    created.append((plan["name"], price.id))

print("✅ Prezzi creati:")
for name, price_id in created:
    print(f"{name}: {price_id}") 
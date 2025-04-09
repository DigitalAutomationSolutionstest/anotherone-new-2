from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.config import settings
from routes import chat, code, transcribe, sitegen, csv, auth, payments, stripe_webhook

app = FastAPI(
    title=settings.APP_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Configurazione CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Includi i router per ogni mini-app
app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(chat.router, prefix=settings.API_V1_STR)
app.include_router(code.router, prefix=settings.API_V1_STR)
app.include_router(transcribe.router, prefix=settings.API_V1_STR)
app.include_router(sitegen.router, prefix=settings.API_V1_STR)
app.include_router(csv.router, prefix=settings.API_V1_STR)
app.include_router(payments.router, prefix=settings.API_V1_STR)
app.include_router(stripe_webhook.router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {
        "message": "Benvenuto nella piattaforma AI",
        "version": "1.0.0",
        "docs_url": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 
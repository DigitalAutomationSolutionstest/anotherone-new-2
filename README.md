# Piattaforma AI Interattiva

Una piattaforma web completa che integra 5 mini-app AI in un'unica dashboard interattiva.

## 🚀 Caratteristiche

- Chatbot AI (Claude + Mistral)
- Generatore Siti Statici
- Assistente Codice
- Trascrizione Audio + Sintesi
- Dashboard Analisi CSV

## 🛠️ Tecnologie Utilizzate

### Backend
- FastAPI (API REST)
- Python 3.9+
- JWT per autenticazione
- Integrazione con varie API AI

### Frontend
- Next.js
- React
- TailwindCSS
- TypeScript

### AI Services
- Claude (Anthropic)
- Mistral (Together.ai)
- Cohere
- Hugging Face
- Whisper

## 🏗️ Installazione

1. Clona il repository:
```bash
git clone https://github.com/yourusername/ai-platform.git
cd ai-platform
```

2. Installa le dipendenze del backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Installa le dipendenze del frontend:
```bash
cd ../frontend
npm install
```

4. Configura le variabili d'ambiente:
```bash
cp backend/.env.example backend/.env
# Modifica backend/.env con le tue API keys
```

## 🚀 Avvio

1. Avvia il backend:
```bash
cd backend
uvicorn main:app --reload
```

2. Avvia il frontend:
```bash
cd frontend
npm run dev
```

3. Apri il browser all'indirizzo: http://localhost:3000

## 🔑 API Keys Richieste

- Anthropic (Claude)
- Together.ai (Mistral)
- Cohere
- Hugging Face
- Supabase (opzionale)

## 📝 Documentazione API

La documentazione Swagger è disponibile all'indirizzo: http://localhost:8000/docs

## 🤝 Contribuire

1. Fai il fork del repository
2. Crea un branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. Committa le tue modifiche (`git commit -m 'Add some AmazingFeature'`)
4. Pusha al branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## 📄 Licenza

Questo progetto è sotto licenza MIT - vedi il file [LICENSE](LICENSE) per i dettagli.

## 👥 Autori

- Il tuo nome - [@tuotwitter](https://twitter.com/tuotwitter)

## 🙏 Ringraziamenti

- Anthropic per Claude
- Together.ai per Mistral
- Cohere
- Hugging Face
- FastAPI team
- Next.js team 
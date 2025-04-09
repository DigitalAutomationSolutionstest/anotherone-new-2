from supabase import create_client, Client
from config.config import settings
from typing import Dict, Any, Optional

class SupabaseService:
    def __init__(self):
        self.supabase: Client = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_KEY
        )
        
    async def sign_up(self, email: str, password: str) -> Dict[str, Any]:
        try:
            response = await self.supabase.auth.sign_up({
                "email": email,
                "password": password
            })
            return response
        except Exception as e:
            raise Exception(f"Errore nella registrazione: {str(e)}")
            
    async def sign_in(self, email: str, password: str) -> Dict[str, Any]:
        try:
            response = await self.supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            return response
        except Exception as e:
            raise Exception(f"Errore nel login: {str(e)}")
            
    async def get_user(self, user_id: str) -> Optional[Dict[str, Any]]:
        try:
            response = await self.supabase.from_("users").select("*").eq("id", user_id).single().execute()
            return response.data
        except Exception as e:
            raise Exception(f"Errore nel recupero utente: {str(e)}")
            
    async def save_chat_log(self, user_id: str, message: str, response: str, model: str) -> Dict[str, Any]:
        try:
            data = {
                "user_id": user_id,
                "message": message,
                "response": response,
                "model": model
            }
            response = await self.supabase.from_("chat_logs").insert(data).execute()
            return response.data[0]
        except Exception as e:
            raise Exception(f"Errore nel salvataggio chat: {str(e)}")
            
    async def save_code_output(self, user_id: str, code: str, description: str) -> Dict[str, Any]:
        try:
            data = {
                "user_id": user_id,
                "code": code,
                "description": description
            }
            response = await self.supabase.from_("code_outputs").insert(data).execute()
            return response.data[0]
        except Exception as e:
            raise Exception(f"Errore nel salvataggio codice: {str(e)}")
            
    async def save_transcription(self, user_id: str, audio_url: str, text: str) -> Dict[str, Any]:
        try:
            data = {
                "user_id": user_id,
                "audio_url": audio_url,
                "text": text
            }
            response = await self.supabase.from_("transcriptions").insert(data).execute()
            return response.data[0]
        except Exception as e:
            raise Exception(f"Errore nel salvataggio trascrizione: {str(e)}")
            
    async def save_csv_analysis(self, user_id: str, csv_url: str, analysis: str) -> Dict[str, Any]:
        try:
            data = {
                "user_id": user_id,
                "csv_url": csv_url,
                "analysis": analysis
            }
            response = await self.supabase.from_("csv_analyses").insert(data).execute()
            return response.data[0]
        except Exception as e:
            raise Exception(f"Errore nel salvataggio analisi CSV: {str(e)}")
            
    async def update_user_role(self, user_id: str, role: str) -> Dict[str, Any]:
        try:
            data = {"role": role}
            response = await self.supabase.from_("users").update(data).eq("id", user_id).execute()
            return response.data[0]
        except Exception as e:
            raise Exception(f"Errore nell'aggiornamento ruolo utente: {str(e)}") 
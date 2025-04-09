import anthropic
import together
from config.config import settings
import httpx
from typing import Dict, Any

class AIService:
    def __init__(self):
        self.anthropic_client = anthropic.Client(api_key=settings.ANTHROPIC_API_KEY)
        together.api_key = settings.TOGETHER_API_KEY
        
    async def get_claude_response(
        self,
        message: str,
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> Dict[str, Any]:
        try:
            response = await self.anthropic_client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{
                    "role": "user",
                    "content": message
                }]
            )
            
            return {
                "text": response.content[0].text,
                "tokens_used": response.usage.total_tokens
            }
            
        except Exception as e:
            raise Exception(f"Errore nella chiamata a Claude: {str(e)}")
            
    async def get_mistral_response(
        self,
        message: str,
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> Dict[str, Any]:
        try:
            response = await together.Complete.create(
                prompt=message,
                model="mistralai/Mixtral-8x7B-Instruct-v0.1",
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            return {
                "text": response["output"]["choices"][0]["text"],
                "tokens_used": response["output"]["usage"]["total_tokens"]
            }
            
        except Exception as e:
            raise Exception(f"Errore nella chiamata a Mistral: {str(e)}")
            
    async def get_cohere_response(
        self,
        text: str,
        task: str = "summarize"
    ) -> Dict[str, Any]:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://api.cohere.ai/v1/generate",
                    headers={
                        "Authorization": f"Bearer {settings.COHERE_API_KEY}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "command",
                        "prompt": text,
                        "max_tokens": 300,
                        "temperature": 0.3
                    }
                )
                
                result = response.json()
                return {
                    "text": result["generations"][0]["text"],
                    "tokens_used": result["meta"]["billed_tokens"]
                }
                
        except Exception as e:
            raise Exception(f"Errore nella chiamata a Cohere: {str(e)}") 
from pydantic import BaseSettings, Field
from typing import Optional

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    openai_api_key: str = Field(..., env='OPENAI_API_KEY')
    model_name: str = Field('gpt-3.5-turbo', env='MODEL_NAME')
    temperature: float = Field(0.7, env='TEMPERATURE')
    max_tokens: int = Field(1000, env='MAX_TOKENS')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()

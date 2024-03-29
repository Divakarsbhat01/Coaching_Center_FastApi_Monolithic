import os
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

class Settings(BaseSettings):
    upstatus:str
    MONGO_connection_url:str
    SQL_ALCHEMY_DATABASE_URL:str
    SECRET_KEY:str
    ALGORITHM:str
    Access_token_expire_time:int
    SQL_USERNAME:str
    SQL_PASSWORD:str
    SQL_HOST_NAME:str
    SQL_DB_nAME:str
    model_config = SettingsConfigDict(env_file=".env")

settings=Settings()

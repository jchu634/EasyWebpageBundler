from typing import Any
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

root = os.path.dirname(os.path.abspath(__file__))

class SettingsModel(BaseSettings):
    ENV: str = "development"
    ERR404: bool = False
    APPNAME:str = "Easy Web Page Bundler"
    STATIC_FOLDER:str = os.path.join(root,"static/")
    model_config = SettingsConfigDict(
        env_file=(
            ".env",
            ".env.production.local",
            ".env.development.local"
        )
    )
    
Settings = SettingsModel()

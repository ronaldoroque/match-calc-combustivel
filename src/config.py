import os
import sys
from functools import lru_cache

import pytz
from pydantic import BaseSettings

tz = pytz.timezone('America/Sao_Paulo')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


class Settings(BaseSettings):

    debug: bool = False
    secret_key: str
    algorithm: str = "HS256"
    allowed_host: str
    allowed_origins: str

    project_name: str = "api"
    version: str = "0.1.0"
    description: str = ""

    log_file_pattern: str
    log_level: str
    log_rotation: str
    log_retention: int

    mapbox_access_token: str = ""

    class Config:
        env_file = f"{BASE_DIR}/.env"


@lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    return settings

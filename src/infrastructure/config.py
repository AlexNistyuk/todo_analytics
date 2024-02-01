import os
from functools import lru_cache
from pathlib import Path

from pydantic import Extra
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE_PATH = os.path.join(BASE_DIR.parent.parent, ".env")


class Settings(BaseSettings):
    db_url: str
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_region: str

    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH, extra=Extra.allow)


@lru_cache
def get_settings():
    return Settings()

# Stdlib Imports
from typing import Union, Any


# Pydantic Imports
from pydantic import BaseSettings

# Third Party Imports
from decouple import config as environ


class Settings(BaseSettings):
    """Environment configurations for backend"""

    DATABASE_URL: Union[str, Any] = environ("DB_URL", cast=str)
    ALLOWED_METHODS: list = ["GET", "POST", "OPTIONS"]
    ALLOWED_CREDENTIALS: bool = True
    XE_ID: Union[str, Any] = environ("XE_ID", cast=str)
    XE_TOKEN: Union[str, Any] = environ("XE_TOKEN", cast=str)


settings = Settings()

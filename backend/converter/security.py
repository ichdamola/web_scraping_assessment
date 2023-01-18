# FastAPI Imports
from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader

# Own Imports
from backend.converter.utils import read_from_apikey_json


#  Define the name of HTTP header to retrieve an API key from
API_KEY_HEADER = APIKeyHeader(name="x-api-key", auto_error=False)


async def get_api_token(api_key: str = Security(API_KEY_HEADER)) -> str:
    """
    This function retrieves & validate an API key from the HTTP header.

    :param token_header: str = Security(API_TOKEN_HEADER)
    :type token_header: str

    :return: The api key is being returned.
    """

    if api_key not in read_from_apikey_json()["keys"]:
        raise HTTPException(400, {"message": "Invalid api key."})
    return api_key

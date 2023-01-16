# FastAPI Imports
from fastapi import APIRouter, Depends

# Own Imports
from backend.converter.security import get_api_token


public_router = APIRouter(tags=["Public"])
private_router = APIRouter(tags=["Private"], dependencies=[Depends(get_api_token)])

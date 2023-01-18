# Uvicorn Imports
import uvicorn

# FastAPI Imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Own Imports
from backend.config.settings import settings
from backend.converter.api import public_router, private_router


# initialize fastapi
app = FastAPI()

# add cors and session middleware
app.add_middleware(
    CORSMiddleware,
    allow_methods=settings.ALLOWED_METHODS,
    allow_credentials=settings.ALLOWED_CREDENTIALS,
)

# include routers
app.include_router(public_router)
app.include_router(private_router)

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=7000, reload=True)

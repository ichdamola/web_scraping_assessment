# Stdlib Imports
from typing import List

# Own Imports
from backend.converter.router import private_router, public_router
from backend.converter.schemas import ConvertSchema

from backend.converter import services
from backend.converter.utils import read_from_apikey_json


@public_router.get("/api-keys")
async def get_apikeys():
    """This API view is responsible for getting the list of available api keys."""

    list_of_keys = read_from_apikey_json()["keys"]
    return {"data": list_of_keys}


@private_router.post("/convert", status_code=201)
async def convert_currency(payload: ConvertSchema):
    """This API view is responsible for converting currencies."""

    conversion_history = await services.convert(
        payload.amount, payload.from_currency, payload.to_currency
    )
    return conversion_history.to_dict()


@private_router.get("/currencies")
async def get_currencies():
    """This API view is responsible for retrieving all the currencies."""

    currencies = services.get_all_currencies()
    return currencies


@private_router.get("/history")
async def get_conversion_histories() -> list:
    """This API view is responsible for retrieving all the conversions histories."""

    conversion_histories = await services.get_all_conversions()
    return conversion_histories

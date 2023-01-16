# Stdlib Imports
from typing import List

# Own Imports
from backend.config.settings import settings
from backend.converter.middle_rate import MiddleRate
from backend.converter.xe_currency import list_of_currencies
from backend.converter.orm import converter_orm, currency_orm
from backend.converter.models import ConversionHistory, Currency


async def convert(
    amount: int, from_currency: str, to_currency: str
) -> ConversionHistory:
    """
    This function converts an amount from X currency, to Y currency,
    and returns a conversion history.

    :param amount: the amount of currency to convert
    :type amount: int
    :param from_currency: The currency you want to convert from
    :type from_currency: str
    :param to_currency: The currency you want to convert to
    :type to_currency: str

    :return: A conversion history object
    """

    # post data to xe website
    # results: the converted amount and rate
    converted_amount, rate = MiddleRate().interback_extracter(
        amount, from_currency, to_currency
    )

    # create converison history
    conversion_history = await converter_orm.create(
        converted_amount, from_currency, to_currency, rate
    )
    return conversion_history


async def fetch_and_create_currencies() -> str:

    xe_currency = Currency()
    currencies = xe_currency.list_of_currencies()
    print(currencies)

    for curr in currencies:
        await currency_orm.create(curr["currency_name"], curr["iso"])

    return "Added currencies to database!"


def get_all_currencies() -> List[Currency]:
    """
    This function returns a list of all the currencies in the database

    :return: A list of all the currencies in the database.
    """

    # await fetch_and_create_currencies()
    # currencies = await currency_orm.get()

    return list_of_currencies()


async def get_all_conversions() -> List[ConversionHistory]:
    """
    This function returns a list of all the conversions in the database.

    :return: A list of all the conversions in the database.
    """

    conversions = await converter_orm.get()
    return conversions

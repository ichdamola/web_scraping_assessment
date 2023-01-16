# Stdlib Imports
from typing import List

# SQLAlchemy Imports
from sqlalchemy.orm import Session

# Own Imports
from backend.config.database import SessionLocal
from backend.converter.models import ConversionHistory, Currency


class ORMSession:
    def __init__(self, db: Session):
        self.orm = db


class ConverterORM(ORMSession):
    async def get(self) -> List[ConversionHistory]:
        """
        This method gets a list of the conversion
        histories from the database.
        """

        conversion_histories = self.orm.query(ConversionHistory).all()
        return conversion_histories

    async def create(
        self, amount: str, from_currency: str, to_currency: str, rate: float
    ) -> ConversionHistory:
        """
        This method creates a conversion history to the database.

        :param amount: The amount of currency to be converted
        :type amount: str
        :param from_currency: The currency to convert from
        :type from_currency: str
        :param to_currency: The currency to convert to
        :type to_currency: str
        :param rate: The rate at which the conversion is done
        :type rate: float

        :return: The conversion history object.
        """

        conversion = ConversionHistory(
            **{
                "converted_amount": amount,
                "from_currency": from_currency,
                "to_currency": to_currency,
                "rate": rate,
            }
        )

        self.orm.add(conversion)
        self.orm.commit()
        self.orm.refresh(conversion)

        return conversion


class CurrencyORM(ORMSession):
    async def get(self) -> list:
        """This method gets a list of currencies from the database."""

        return self.orm.query(Currency).all()

    async def create(self, currency: str, code: str) -> Currency:
        """
        This method create a new currency to the database.

        :param currency: str
        :type currency: str
        :param code: The currency code
        :type code: str

        :return: Currency object
        """

        currency = Currency(**{"currency": currency, "currency_code": code})

        self.orm.add(currency)
        self.orm.commit()
        self.orm.refresh(currency)

        return currency


converter_orm = ConverterORM(SessionLocal())
currency_orm = CurrencyORM(SessionLocal())

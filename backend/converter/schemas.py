# Stdlib Imports
from datetime import datetime

# Pydantic Imports
from pydantic import BaseModel


class BaseSchema(BaseModel):
    from_currency: str
    to_currency: str


class ConvertSchema(BaseSchema):
    amount: int


class CurrencySchema(BaseModel):
    currency: str
    currency_code: str

    class Config:
        orm_mode = True


class ConversionSchema(BaseSchema):
    id: int
    converted_amount: str
    rate: float
    time_of_conversion: datetime

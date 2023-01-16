# Stdlib Imports
from datetime import datetime
from typing import Dict, Any

# SQLAlchemy Imports
from sqlalchemy import Column, Float, String, DateTime, Integer

# Own Imports
from backend.config.database import Base


class ConversionHistory(Base):
    __tablename__ = "conversion_histories"

    id = Column(Integer, primary_key=True, index=True)
    converted_amount = Column(String)
    rate = Column(Float, default=0.0)
    time_of_conversion = Column(DateTime, default=datetime.now)
    from_currency = Column(String)
    to_currency = Column(String)

    def __str__(self) -> str:
        return f"Conversion for {self.from_currency}"

    def to_dict(self) -> Dict[str, Any]:
        data = self.__dict__
        return {
            "converted_amount": data["converted_amount"],
            "rate": data["rate"],
            "metadata": {
                "time_of_conversion": data["time_of_conversion"],
                "from_currency": data["from_currency"],
                "to_currency": data["to_currency"],
            },
        }


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    currency = Column(String)
    currency_code = Column(String(3))

    def __str__(self) -> str:
        return self.currency.__str__()

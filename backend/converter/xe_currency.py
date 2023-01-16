# Stdlib Imports
from typing import List, Dict, Any

# Third Party Imports
import httpx


def list_of_currencies() -> List[Dict[str, Any]]:
    """
    This function returns a list of dictionaries, each of which contains
    information about a currency.

    :return: A list of dictionaries.
    """

    currencies = [
        {
            "Japanese Yen": "JPY",
        },
        {
            "Kenyan Shilling": "KES",
        },
    ]
    return currencies


print(list_of_currencies())

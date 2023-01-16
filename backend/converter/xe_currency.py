# Stdlib Imports
from typing import List, Dict, Any

# Third Party Imports
import httpx


class Currency:
    def __init__(self, token: str, id: str):
        self.token = token
        self.id = id

    def list_of_currencies(self) -> List[Dict[str, Any]]:
        """
        This function returns a list of dictionaries, each of which contains 
        information about a currency.
        
        :return: A list of dictionaries.
        """
        
        url = "https://xecdapi.xe.com/v1/currencies"
        res = httpx.get(url, auth=(self.id, self.token))
        currencies = res.json()["currencies"]
        return currencies

# Stdlib Imports
import re
from typing import Tuple

# Third Party Imports
import certifi, urllib3
from bs4 import BeautifulSoup


class MiddleRate:
    def interback_extracter(self, amount: int, fro: str, to: str) -> Tuple:
        """
        This method takes in the amount, the currency to convert from
        and the currency to convert to, and returns
        the converted amount and the rate.

        :param amount: The amount of currency you want to convert
        :type amount: int
        :param fro: The currency you want to convert from
        :type fro: str
        :param to: The currency you want to convert to
        :type to: str

        :return: A tuple of the converted amount and the rate.
        """

        url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={fro}&To={to}"
        req = urllib3.PoolManager(
            cert_reqs="CERT_REQUIRED", ca_certs=certifi.where()
        )
        res = req.request("GET", url)
        soup = BeautifulSoup(res.data, "html.parser")

        # Finding all the elements with the class names:
        # "result__BigRate-sc-1bsijpp-1 iGrAod" and
        # "unit-rates___StyledDiv-sc-1dk593y-0 dEqdnx"
        amount_contents = soup.find_all(
            class_="result__BigRate-sc-1bsijpp-1 iGrAod"
        )
        rate_contents = soup.find_all(
            class_="unit-rates___StyledDiv-sc-1dk593y-0 dEqdnx"
        )

        # get converted amount and rate
        converted_amount = self.parser(amount_contents).split()[0]
        rate = self.parser(rate_contents).split()[3]

        return converted_amount, rate

    def parser(self, content: list) -> str:
        """
        Parse a string of characters to extract any
        character(s) occuring once or multiple times between '>' & '<'.

        content: str
        """
        pattern = r"(?<=\>).+?(?=\<)"
        return "".join(re.findall(pattern, str(content)))

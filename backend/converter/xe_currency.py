# Stdlib Imports
import re
from typing import List, Dict, Any

# Thirdparty Imports
import certifi
import urllib3
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def list_of_currencies() -> List[Dict[str, Any]]:
    """
    This function returns a list of dictionaries, each of which contains
    information about a currency.

    :return: A list of dictionaries.
    """
    url = "https://help.xe.com/hc/en-gb/articles/4408840388753-Which-currencies-do-you-offer-"
    # Start a webdriver instance
    driver = webdriver.Chrome()

    # Navigate to the specified URL
    driver.get(url)

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Get the HTML content of the page
    html = driver.page_source

    # Close the webdriver
    driver.quit()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Find all 'span' tags with class='wysiwyg-color-black'
    wysiwyg_color_black = soup.find_all("span", class_="wysiwyg-color-black")

    # Extract the text from each tag and return as a list
    return [
        {
            tag.get_text()
            .split("(")[0]: tag.get_text()
            .split("(")[1]
            .split(")")[0]
        }
        for tag in wysiwyg_color_black
    ]

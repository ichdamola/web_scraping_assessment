import json


def read_from_apikey_json() -> dict:
    """
    This function opens the file `api_keys.json` and reads
    the contents of the file into a variable called `API_KEYS`.

    :return: A dictionary of API keys
    """

    with open("api_keys.json") as api_keys:
        API_KEYS = json.load(api_keys)
    return API_KEYS

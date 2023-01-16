# Steps to Run the Project:
1. Rename the .env.template file to .env and change the variables as below:
```
DB_URL=sqlite:///./currency_converter.sqlite
XE_ID=pandawaretech314144122
XE_TOKEN=o10eanv092m7sll7gq3c6eidg9
```

2. Rename api_keys.json.template to api_keys.json and the variables as below:
```
{
    "keys": [
        "sk_86cb2858ee371881a336114bb2acdc5e",
        "sk_35283e7e97fb43c98d164ee3e9be4f3c",
        "sk_0ece6f7e57a4437dc31c9467b7dw7nw0"
    ]
}
```
3. Pip install the requirements.txt file using the cmd:
```pip install -r requirements.txt```
4. And then finally, run python -m backend/main.py to start the server using the cmd:
```python -m backend/main.py```
#BASED ON TUTORIAL: https://www.dataquest.io/blog/python-api-tutorial/

#In commandline create virtual environment
#> python -m  venv myvenv
#> myvenv\Scripts\activate

install requests

import requests

#example no 1
response = requests.get("https://bdl.stat.gov.pl/api/v1/Units?level=2.json")

print(response.status_code)

print(response.json())

#convert object to string
import json

def print_json(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print_json(response.json())



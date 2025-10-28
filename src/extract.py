import requests
import os
from dotenv import load_dotenv
from pprint import pprint 
import json

load_dotenv()

def extract(event=os.getenv("DEFAULT_EVENT")):
    event = json.loads(event) 
    params = event["params"]
    headers = json.loads(event["api_key"])
    url = event["url"]
    response = requests.get(url, headers=headers, params=params)
    return response

if __name__ =="__main__":
    pprint(extract().json())
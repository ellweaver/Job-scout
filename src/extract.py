import requests
import os
from dotenv import load_dotenv

def extract(event=os.getenv["DEFAULT_EVENT"]):
    
    params=event["params"]
    headers = event["api_key"]
    url = event["url"]
    response=requests.get(url,   params=params, headers=headers)
    return response
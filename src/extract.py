import requests
import os
from dotenv import load_dotenv
from pprint import pprint 
import json
load_dotenv()

def extract(event=os.getenv("DEFAULT_EVENT")):
    print(event)
    event=json.loads(event) 
    params=event["params"]
    headers = event["api_key"]
    print(headers)
    url = event["url"]
    response=requests.get(url,   params=params, headers=headers)
    return response

if __name__ =="__main__":
    pprint(extract())
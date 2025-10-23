import requests
import os
from dotenv import load_dotenv

def extract(event=os.getenv["DEFAULT_EVENT"]):
    
    params={"query":event["query"]}
    requests.get()
    return "something"
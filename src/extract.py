import requests
import os
from dotenv import load_dotenv

def extract(event=os.getenv["DEFAULT_EVENT"]):
    
    params={event["params"]}
    
    requests.get()
    return "something"
from src.extract import extract
import json
import os
from dotenv import load_dotenv
load_dotenv()

def query():
    pass


def perform_search(filepath="./json_files/default_event.json", api_key=os.getenv("API_KEY")):
    """ 
    Turns Json File into event string and inputs string into extract function.
    """
    with open(filepath) as f:
        event= json.dump(f)
    event["api_key"] = api_key
    json.dumps(event)
    response=extract(event)
    return response
    
def generate_search():
    pass
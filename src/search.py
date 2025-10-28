from src.extract import extract
import json
import os
from dotenv import load_dotenv
load_dotenv()

def query():
    pass


def perform_search(search_filepath="./json_files/default_event.json", api_key=os.getenv("API_KEY"), destination_filepath="./search_results/default_destination.json"):
    """ 
    Turns Json File into event string and inputs string into extract function.
    """
    with open(search_filepath) as f:
        event= json.load(f)   
    event["api_key"] = api_key
    event=json.dumps(event)
    response=extract(event)

    with open(destination_filepath, 'w') as f:
        f.write(str(response.json()))

    return response
    
def generate_search(
        url="https://api.openwebninja.com/jsearch/search",
        query="", page=1, num_pages=1, country="gb", language="en"):
    '''
    Console tool to create a json file which can be used for perform_search
    '''
    event = {"api_key": {}, "url":"https://api.openwebninja.com/jsearch/search","params":{"query":"junior python"}}
    
    input()
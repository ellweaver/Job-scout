from src.extract import extract
import json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()




def perform_search(
    search_directory="./search_queries/",
    search_filename="default_search.json",
    api_key=os.getenv("API_KEY"),
    destination_directory="./search_results/"
):
    """
    Turns Json File into event string and inputs string into extract function.
    """
    search_filepath = search_directory + search_filename
    
    with open(search_filepath) as f:
        event = json.load(f)

    event["api_key"] = {"x-api-key": api_key}

    response = extract(event)
    destination_timestamp = str(datetime.now())
    destination_filepath = destination_directory + destination_timestamp + " " + search_filename
    
    with open(destination_filepath, "w") as f:
        f.write(json.dumps(response.json(), indent=4))

    return response

def manual_search():
    """_summary_

    queries user for 4 inputs:
    - source directory
    - source filename
    - destination directory
    - api token
    """

    search_directory = str(input("Please enter the directory for your search file [./search_queries/]: ")).strip()
    search_filename = str(input("Please enter the filename of your search file [default_search.json]: ")).strip()
    destination_directory = str(input("Please enter an existing save location for your query [./search_results/]: ")).strip()
    api_token = str(input("Please enter your OpenWeb Ninja API token [.env]: ")).strip()

    params = {
        "search_directory": search_directory,
        "search_filename": search_filename,
        "destination_directory": destination_directory,
        "api_token": api_token
    }

    not_none_params = {k:v for k, v in params.items() if v}

    return perform_search(**not_none_params)

def generate_search_file(
    url="https://api.openwebninja.com/jsearch/search",
    query="",
    file_name="",
    search_directory="search_queries/",
    page=1,
    num_pages=1,
    country="gb",
    language="en",
    date_posted="all",
    work_from_home=False,
    employment_types=["FULLTIME", "CONTRACTOR", "PARTTIME", "INTERN"],
    job_requirements=None,
    radius=25,
    exclude_job_publishers=None,
    fields=None,
):
    """
    Console tool to create a json file which can be used for perform_search also returns event dict
    """
    event = {
        "api_key": {},
        "url": url,
        "params": {"query": "", "page":page, "num_pages":num_pages, "country":country,"language":language,"date_posted":date_posted,"work_from_home":work_from_home,"employment_types":employment_types,"radius":radius}
    }
    while not query:
        query=input("Enter your search Query: ")
    event["params"]["query"] =query
    

    while not file_name:
        file_name=input("Please enter your Search file name without extension: ").lstrip()
    
    file_name= file_name+".json"
        
    search_filepath=search_directory+file_name
    
    
    with open(search_filepath, "w")as f:
        f.write(json.dumps(event, indent=4))

    return {"event":event, "search_directory":search_directory,"filename":file_name,"filepath":search_filepath}

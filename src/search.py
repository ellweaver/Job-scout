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

    search_directory = input("Please enter the directory for your search file [./search_queries/]: ").strip()
    search_filename = input("Please enter the filename of your search file [default_search.json]: ").strip()
    destination_directory = input("Please enter an existing save location for your query [./search_results/]: ").strip()
    api_token = input("Please enter your OpenWeb Ninja API token [.env]: ").strip()

    params = {
        "search_directory": search_directory,
        "search_filename": search_filename,
        "destination_directory": destination_directory,
        "api_token": api_token
    }

    not_none_params = {k:v for k, v in params.items() if v}

    return perform_search(**not_none_params )

def generate_search_file(
    url="https://api.openwebninja.com/jsearch/search",
    query="",
    file_name="",
    search_directory="search_queries/",
    page="1",
    num_pages="1",
    country="gb",
    language="en",
    date_posted="all",
    work_from_home=False,
    employment_types="FULLTIME,CONTRACTOR,PARTTIME,INTERN",
    job_requirements="",
    radius="25",
    exclude_job_publishers="",
    fields="",
    advanced=False
):
    """
    Console tool to create a json file which can be used for perform_search also returns event dict
    """
    
    while not query:
        query = input("Enter your search Query: ")
    
    if advanced == True:

        user_response = input("page [1]: ").strip()
        if user_response:
            page=user_response

        user_response = input("number of pages [1]: ").strip()
        if user_response:
            num_pages=user_response

        user_response = input("country [gb]: ").strip()
        if user_response:
            country=user_response

        user_response = input("language [en]: ").strip()
        if user_response:
            language=user_response

        user_response = input("date posted [all]: ").strip()
        if user_response:
            date_posted=user_response

        user_response = input("work from home [False]: ").strip().lower().startswith('t')
        if user_response:
            work_from_home=user_response

        user_response=input('employment types ["FULLTIME", "CONTRACTOR", "PARTTIME", "INTERN"]: ').strip()
        if user_response:
            employment_types=user_response

        user_response = input("job requirements []: ").strip()
        if user_response:
            job_requirements=user_response

        user_response = input("radius [25]: ").strip()
        if user_response:
            radius=user_response

        user_response = input("exclude job publishers []: ").strip()
        if user_response:
            exclude_job_publishers=user_response

        user_response = input("fields []: ").strip()
        if user_response:
            fields=user_response

    params = {
        "query": query,
        "page": page,
        "num_pages": num_pages,
        "country": country,
        "language": language,
        "date_posted": date_posted,
        "work_from_home": work_from_home,
        "employment_types": employment_types,
        "job_requirements": job_requirements,
        "radius": radius,
        "exclude_job_publishers": exclude_job_publishers,
        "fields": fields
        }

    not_none_params = {k:v for k, v in params.items() if v is not "" and v is not []}

    event = {
        "api_key": {},
        "url": url,
        "params": not_none_params
    }
    
    while not file_name:
        user_response = input(f"Please enter your Search file name without extension[{query}]: ").lstrip()
        if  user_response:
            file_name = user_response
        else:
            file_name = query

    
    file_name = file_name + ".json"
        
    search_filepath = search_directory + file_name
    
    with open(search_filepath, "w") as f:
        f.write(json.dumps(event, indent=4))

    return {"event": event, "search_directory": search_directory, "filename": file_name, "filepath": search_filepath}

def list_search_directory(search_directory="search_queries/"):
    """lists all files in specified directory returns file path chosen by user input check file has url and params keys and query key in params """



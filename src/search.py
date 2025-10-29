from src.extract import extract
import json
import os
from dotenv import load_dotenv

load_dotenv()


def query():
    """
    queries whether we want to immediately perform a search, calling a file or using existing defaults
    or
    generate search
    """
    pass


def perform_search(
    search_filepath="./json_files/default_event.json",
    api_key=os.getenv("API_KEY"),
    destination_filepath="./search_results/default_destination.json",
):
    """
    Turns Json File into event string and inputs string into extract function.
    """

    with open(search_filepath) as f:
        event = json.load(f)

    event["api_key"] = {"x-api-key": api_key}

    response = extract(event)

    with open(destination_filepath, "w") as f:
        f.write(str(response.json()))

    return response


def generate_search_file(
    url="https://api.openwebninja.com/jsearch/search",
    query="",
    search_filepath="/json_files/user_event.json",
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
        "url": "https://api.openwebninja.com/jsearch/search",
        "params": {"query": "junior python"},
    }

    return {}

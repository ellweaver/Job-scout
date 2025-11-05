from src.search import perform_search, generate_search_file
from test_json.json_example import ninja_response
from unittest.mock import Mock
import json
import pytest
from freezegun import freeze_time
from datetime import datetime

class TestPerformSearch:
    
    @freeze_time("2025-01-31")
    @pytest.mark.it("extract called with correct event")
    def test_search_calls_extract_correctly(self, mock_response, monkeypatch):
        class MiniMockResponse(Mock):
            @staticmethod
            def json():
                return ninja_response

            @staticmethod
            def status_code():
                return 200

        mock = MiniMockResponse()

        monkeypatch.setattr("src.search.extract", mock)

        test_api_token = "TEST_API"
        test_search_results_directory="./test/test_json/"

        user_query = "test query in london"
        file_name = "test_search_query"

        test_event = {"api_key": {"x-api-key": "TEST_API"}, "url": "https://api.openwebninja.com/jsearch/search", "params": {"query": "test query in london", "page": "1", "num_pages": "1", "country": "gb", "language": "en", "date_posted": "all", "work_from_home": False, "employment_types": "FULLTIME,CONTRACTOR,PARTTIME,INTERN", "radius": "25"}}
        
        filepath = generate_search_file(query=user_query, file_name=file_name, search_directory="./test/test_json/")
        search_directory= filepath["search_directory"]
        search_filename=filepath["filename"]
        perform_search(search_directory,search_filename, test_api_token, test_search_results_directory)

        mock.assert_called_with(test_event)
    
    @freeze_time("2025-01-31")
    @pytest.mark.it("perform search returns correct response")
    def test_search_returns_correct_response(self, mock_response):
        test_api_token = "TEST_API"
        test_search_results_directory="./test/test_json/"

        user_query = "test query in london"
        file_name = "test_search_query"

        filepath = generate_search_file(query=user_query, file_name=file_name, search_directory="./test/test_json/")
        search_directory= filepath["search_directory"]
        search_filename=filepath["filename"]

        response = perform_search(search_directory, search_filename, test_api_token, test_search_results_directory)

        assert isinstance(response.json(), dict)
        assert isinstance(response.status_code, int)

    @freeze_time("2025-01-31")
    @pytest.mark.it("Test that extract response saves in expected location")
    def test_search_saves_response(self, mock_response, monkeypatch):
        user_filename = "test_search_query"
        user_query = "test query in Jamaica"
        test_api_token = "TEST_API"
        destination_directory = "./test/test_json/"
        destination_timestamp=str(datetime.now())
        monkeypatch.setattr('builtins.input', lambda _:user_filename)
        
        search_filepath = generate_search_file(query=user_query, search_directory="./test/test_json/")
        search_directory= search_filepath["search_directory"]
        search_filename=search_filepath["filename"]

        perform_search(
            search_directory=search_directory,
            search_filename=search_filename,
            api_key=test_api_token,
            destination_directory=destination_directory)

        destination_filepath=destination_directory+destination_timestamp+" "+user_filename+".json"
        with open(destination_filepath, "r") as f:
            results_file = f.read()
        
        assert json.loads(results_file) == ninja_response


class TestGenerateSearchFile:
    @pytest.mark.it('Generate_search_file returns dictionary')
    def test_generate_search_file_dict(self,monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _:"test query in london")
        assert isinstance(generate_search_file(search_directory="./test/test_json/" ,file_name="test_search_query"), dict)
    
    @pytest.mark.it('Generate_search_file returns correct result')
    def test_Generate_search_file_result(self, monkeypatch):
        user_query="test query in london"
        monkeypatch.setattr('builtins.input', lambda _:user_query)
        test_event={
        "api_key": {},
        "url": "https://api.openwebninja.com/jsearch/search",
        "params": {"query": "test query in london", "page":"1", "num_pages":"1", "country":"gb","language":"en","date_posted":"all","work_from_home":False,"employment_types":"FULLTIME,CONTRACTOR,PARTTIME,INTERN","radius":"25"}
    }
        assert generate_search_file(search_directory="./test/test_json/", file_name="test_search_query")["event"] == test_event

    @pytest.mark.it('Generate_search_file returns correct filepath from user input')
    def test_generate_search_file_filepath(self,monkeypatch):
        user_filename="test_search_query"
        user_query="test query in london"
        monkeypatch.setattr('builtins.input', lambda _:user_filename)
        assert generate_search_file(query=user_query, search_directory="./test/test_json/")["filepath"] =="./test/test_json/test_search_query.json"

    @pytest.mark.it('Test that generated search parameter file saves in expected location')
    def test_file_save(self, monkeypatch):
        user_filename = "test_search_query"
        user_query = "test query in Jamaica"
        monkeypatch.setattr('builtins.input', lambda _:user_filename)
        test_file="""{
    "api_key": {},
    "url": "https://api.openwebninja.com/jsearch/search",
    "params": {
        "query": "test query in Jamaica",
        "page": "1",
        "num_pages": "1",
        "country": "gb",
        "language": "en",
        "date_posted": "all",
        "work_from_home": false,
        "employment_types": "FULLTIME,CONTRACTOR,PARTTIME,INTERN",
        "radius": "25"
    }
}"""
        
        filepath = generate_search_file(query=user_query, search_directory="./test/test_json/")['filepath']

        with open(filepath, "r") as f:
            search_file = f.read()

        assert search_file == test_file

    @pytest.mark.it('generate search file runs advanced checks with inputs and generates params correctly')
    def test_generate_advanced (self, monkeypatch):
        inputs= iter(["test query in Japan", "2", "2", "us", "de", "all", "True","FULLTIME,CONTRACTOR,INTERN", "no_degree", "15", "beeBe,Dice", "employer_name,job_publisher,job_title,job_country" ])
        monkeypatch.setattr('builtins.input', lambda _:next(inputs))
        response = generate_search_file(advanced=True, file_name="test_search_query",search_directory="./test/test_json/")
        assert response["event"]["params"]=={
        "query": "test query in Japan",
        "page": "2",
        "num_pages": "2",
        "country": "us",
        "language": "de",
        "date_posted": "all",
        "work_from_home": True,
        "employment_types": "FULLTIME,CONTRACTOR,INTERN",
        "job_requirements": "no_degree",
        "radius": "15",
        "exclude_job_publishers": "beeBe,Dice",
        "fields": "employer_name,job_publisher,job_title,job_country"
        }

    @pytest.mark.it('Generate search file does not enter advanced params when input is empty')
    def test_generate_advanced_empty_params (self, monkeypatch):
        inputs= iter(["test_search_query", "", "", "", "", "", "","", "", "", "", "", "" ])
        monkeypatch.setattr('builtins.input', lambda _:next(inputs))
        response = generate_search_file(advanced=True, search_directory="./test/test_json/")
        assert response["event"]["params"]=={
        "query": "test_search_query",
        "page": "1",
        "num_pages": "1",
        "country": "gb",
        "language": "en",
        "date_posted": "all",
        "work_from_home": False,
        "employment_types": "FULLTIME,CONTRACTOR,PARTTIME,INTERN",
        "radius": "25",
        }
        assert response["filename"] == "test_search_query.json"
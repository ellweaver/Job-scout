from src.search import query, perform_search, generate_search_file
import pytest
from test_json.json_example import ninja_response
from src.extract import extract
from unittest.mock import Mock


class TestPerformSearch:
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

        file = "test/test_json/test_json.json"
        test_api = "TEST_API"
        test_file="./test/test_json/test_results.json"

        test_event = {
            "api_key": {"x-api-key": "TEST_API"},
            "url": "https://api.openwebninja.com/jsearch/search",
            "params": {"query": "junior python"},
        }

        perform_search(file, test_api, test_file)
        mock.assert_called_with(test_event)

    @pytest.mark.it("perform search returns correct response")
    def test_search_returns_correct_response(self, mock_response):
        file = "test/test_json/test_json.json"
        test_api = {"x-api-key": "TEST_API"}
        test_file="./test/test_json/test_results.json"

        response = perform_search(file, test_api, test_file)
        assert isinstance(response.json(), dict)
        assert isinstance(response.status_code, int)


class TestGenerateSearchFile:
    @pytest.mark.it('Generate_search_file returns dictionary')
    def test_generate_search_file_dict(self):
        assert isinstance(generate_search_file(),dict)

from src.search import query, perform_search, generate_search
import pytest
from json_files.json_example import ninja_response
from src.extract import extract
from unittest.mock import Mock

class TestPerformSearch:
    @pytest.mark.it('extract called with correct event')
    def test_search_calls_extract_correctly(self, mock_response, monkeypatch):
        class MiniMockResponse(Mock):
            @staticmethod
            def json():
                return ninja_response
            
            @staticmethod
            def status_code():
                return 200
            
        mock = MiniMockResponse()

        monkeypatch.setattr("src.extract",  mock)
        
        file= "./test/test_json.json"
        test_api={"x-api-key":"TEST_API"}
        test_event='{"api_key": {"x-api-key":"TEST_API"}, "url":"https://api.openwebninja.com/jsearch/search","params":{"query":"junior python"}}'
        
        perform_search(file, test_api)
        mock.assert_called_with(test_event)
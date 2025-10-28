from json_files.json_example import ninja_response
import pytest
import requests
from unittest.mock import Mock
from src.extract import extract


class TestExtract:
    @pytest.mark.it("extract function returns correct response")
    def test_extract_response(self, mock_response):

        test_event = {
            "api_key": {"x-api-key": "TEST_API"},
            "url": "https://api.openwebninja.com/jsearch/search",
            "params": {"query": "junior python"},
        }

        assert isinstance(extract(test_event).json(), dict)
        assert isinstance(extract(test_event).status_code, int)

    @pytest.mark.it("extract function is called with the correct arguments")
    def test_extract_arguments(self, monkeypatch):
        event = {
            "url": "https://api.openwebninja.com/jsearch/search",
            "api_key": {"x-api-key": "TEST KEY"},
            "params": {"query": "junior python"},
        }

        class MiniMockResponse(Mock):
            @staticmethod
            def json():
                return ninja_response

            @staticmethod
            def status_code():
                return 200

        mock = MiniMockResponse()

        monkeypatch.setattr(requests, "get", mock)

        extract(event)

        mock.assert_called_with(
            "https://api.openwebninja.com/jsearch/search",
            headers={"x-api-key": "TEST KEY"},
            params={"query": "junior python"},
        )

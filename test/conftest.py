from json_files.json_example import ninja_response
import pytest 
import requests 
from unittest.mock import Mock

@pytest.fixture
def mock_response(monkeypatch):
    def mock_get(*args, **kwargs):
        def mock_json():
            return ninja_response
    
            

        mock = Mock(spec=requests.get)
        mock.status_code = 200
        mock.json = mock_json
        return mock

    monkeypatch.setattr(requests, "get", mock_get)



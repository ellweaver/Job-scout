from json_files.json_example import ninja_response
import pytest 
import requests 
from unittest.mock import Mock
from src.extract import extract

class TestExtract:
    @pytest.mark.it('extractfunction returns string value')
    def test_extract_string(self, mock_response):
        assert isinstance(extract(), str)

    
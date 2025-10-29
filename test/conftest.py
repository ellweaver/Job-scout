from test_json.json_example import ninja_response
import pytest
import requests
from unittest.mock import Mock


class MockResponse(Mock):
    @staticmethod
    def json():
        return ninja_response

    @staticmethod
    def status_code():
        return 200

    def __init__(
        self,
        spec=None,
        side_effect=None,
        return_value=...,
        wraps=None,
        name=None,
        spec_set=None,
        parent=None,
        _spec_state=None,
        _new_name="",
        _new_parent=None,
        **kwargs
    ):
        super().__init__(
            spec,
            side_effect,
            return_value,
            wraps,
            name,
            spec_set,
            parent,
            _spec_state,
            _new_name,
            _new_parent,
            **kwargs
        )
        self.status_code = 200


@pytest.fixture
def mock_response(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

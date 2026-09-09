import pytest
from qa_demo.config import load_settings
from qa_demo.api.client import ApiClient

@pytest.fixture(scope="session")
def settings():
    return load_settings()

@pytest.fixture(scope="session")
def api_client(settings):
    return ApiClient(settings.base_url)

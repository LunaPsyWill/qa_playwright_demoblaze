import pytest
import os
from mock_backend.api.client import APIClient
from mock_backend.services.user_service import UserService
from mock_backend.services.login_service import UserLogin

@pytest.fixture
def base_url():
	url = os.getenv("FAKE_API")
	return url

@pytest.fixture
def client(base_url):
	return APIClient(base_url)

@pytest.fixture
def user_service(client):
	return UserService(client)

@pytest.fixture
def login_service(client):
	return UserLogin(client)
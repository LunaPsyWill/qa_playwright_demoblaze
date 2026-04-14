from unittest.mock import MagicMock
import pytest
from mock_backend.services.user_service import UserService
from mock_backend.api.custom_exceptions import APIError

def test_get_user_error():
	mock_client = MagicMock()
	mock_response = MagicMock()

	data = {'nombre': 'usuario'}

	mock_response.json.return_value = data
	mock_client.get.return_value = mock_response

	service = UserService(mock_client) 

	with pytest.raises(KeyError,match="No password"):
		service.get_user(1)
from unittest.mock import MagicMock
from mock_backend.services.user_service import UserService
from mock_backend.api.endpoints import USERS
from mock_backend.api.custom_exceptions import APIError
from mock_backend.factories.user_factory import UserFactory
import pytest

def test_user_service():
	mock_client = MagicMock()
	mock_response = MagicMock()

	factory = UserFactory()
	user = factory.valid_user()

	mock_response.json.return_value = user
	mock_client.post.return_value = mock_response

	service = UserService(mock_client)
	response = service.register_user(user)

	mock_client.post.assert_called_once_with('/users/',json=user)

def test_user_service_error():
	mock_client = MagicMock()

	mock_client.post.side_effect = APIError("Invalid password")

	service = UserService(mock_client)

	with pytest.raises(APIError,match="Invalid password"):
		service.register_user(1)
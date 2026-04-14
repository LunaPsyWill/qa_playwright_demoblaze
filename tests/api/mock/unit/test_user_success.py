from unittest.mock import MagicMock
from mock_backend.services.user_service import UserService

def test_get_user_success():
	mock_client = MagicMock()
	mock_response = MagicMock()

	mock_response.status_code = 200
	mock_response.json.return_value = {'name': 'William','password':12345}

	mock_client.get.return_value = mock_response

	service = UserService(mock_client)
	response = service.get_user(1)

	assert response.json()['name'] == 'William'

	mock_client.get.assert_called_once_with("/users/1")
	assert response.status_code == 200
	
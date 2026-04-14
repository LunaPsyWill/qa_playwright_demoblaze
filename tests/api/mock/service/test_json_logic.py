from mock_backend.factories.user_factory import UserFactory
from mock_backend.services.user_service import UserService
import requests
from mock_backend.api.endpoints import USERS
import pytest

def test_user_created(user_service,requests_mock,base_url):
	#----- CREAR USUARIO
	factory = UserFactory()
	user = factory.valid_user()

	#----- REQUESTS MOCK
	requests_mock.post(
		f"{base_url}{USERS}",
		json={
			"data": user, 
			"created": True
			},
		status_code = 201
		)

	#----- SERVICE
	response = user_service.register_user(user)
	data = response.json()['data']

	assert response.status_code == 201
	assert response.json()['created'] is True

def test_user_not_created(user_service,requests_mock,base_url):
	factory = UserFactory()
	user = factory.valid_user()

	requests_mock.post(
		f"{base_url}{USERS}",
		json={
			"data": user,
			"created": False
			}
		)

	with pytest.raises(ValueError, match="user not created"):
		user_service.register_user(user)

def test_user_no_password(user_service,requests_mock,base_url):
	factory = UserFactory()
	user = factory.invalid_user_no_password()

	requests_mock.post(
		f"{base_url}{USERS}",
		json={
			"data": user
			}
		)

	with pytest.raises(KeyError, match="password does not exist"):
		user_service.register_user(user)
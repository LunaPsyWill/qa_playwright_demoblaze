from mock_backend.factories.user_factory import UserFactory
from mock_backend.services.user_service import UserService
import requests
from mock_backend.api.endpoints import USERS

def test_user_registration(user_service,requests_mock,base_url):
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

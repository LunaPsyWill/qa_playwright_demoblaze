from jsonschema import validate
from mock_backend.schemas.user_schema import user_schema
import requests
from mock_backend.api.endpoints import USERS

def test_get_single_user(user_service,requests_mock,base_url):
	requests_mock.get(
		f"{base_url}{USERS}2",
		json={
			"data":{
				"id": 2,
				"email": "email@dom.com",
				"username": "Ricky123",
				"first_name": "Rick",
				"last_name": "Morty",
				"password": 12345
				}
			},
		status_code=200
		)

	response = user_service.get_user(2)

	assert response.status_code == 200
	assert response.elapsed.total_seconds() < 1

	data = response.json()
	validate(instance=data,schema=user_schema)

	assert data["data"]["id"] == 2

def test_create_user(user_service,requests_mock,base_url):
	user = {
		"id": 2,
		"email": "email@dom.com",
		"username": "Rick",
		"last_name": "Morty",
		"password": 12345
		}

	requests_mock.post(
		f"{base_url}{USERS}",
		json=user,
		status_code=201
		)

	response = user_service.register_user(user)

	assert response.status_code == 201
	data = response.json()

	assert data["username"] == "Rick"
	assert data["password"] == 12345
from jsonschema import validate
from mock_backend.api.endpoints import LOGIN
from mock_backend.schemas.login_schema import login_schema
import requests

def test_login_success(login_service,requests_mock,base_url):
	requests_mock.post(
		f"{base_url}{LOGIN}",
		json={
			"username": "Rick",
			"password": 12345,
			"token": "token"
			},
		status_code=200
		)

	response = login_service.make_login()

	assert response.status_code == 200
	assert response.elapsed.total_seconds() < 1

	data = response.json()
	validate(instance=data,schema=login_schema)
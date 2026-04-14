from mock_backend.api.endpoints import LOGIN
import os

class UserLogin:
	def __init__(self,client):
		self.client = client

	def params(self):
		username = os.getenv("USERNAME_API")
		password = os.getenv("PASSWORD")

		headers = {
			"Content-type": "application/json"
		}
		
		payload = {
			"username": username,
			"password": password
		}

		return headers,payload

	def make_login(self):
		headers,payload = self.params()
		
		response = self.client.post(LOGIN,headers=headers,json=payload)
		return response
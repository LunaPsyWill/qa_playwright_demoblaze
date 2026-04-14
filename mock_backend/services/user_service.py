from mock_backend.api.endpoints import USERS
from mock_backend.api.custom_exceptions import APIError
from mock_backend.factories.user_factory import UserFactory

class UserService:
	def __init__(self,client):
		self.client = client

	def get_user(self,user_id):
		response = self.client.get(f"{USERS}{user_id}")

		data = response.json()

		if data.get("data"):
			return response
		
		if not data.get("password"):
			raise KeyError("No password")

		return response

	def register_user(self,payload):
		response = self.client.post(USERS,json=payload)

		data = response.json()

		if not data.get("data") and data.get("username") and data.get("password"):
			return response

		if not data["data"].get("password"):
			raise KeyError("password does not exist")

		if not data.get("created"):
			raise ValueError("user not created")

		return response
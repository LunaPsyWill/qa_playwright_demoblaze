import random
import string

class UserFactory:
	def valid_user(self):
		return {
			"id": 123,
			"username": self._random_username(),
			"password": "Password123!"
		}

	def invalid_user_short_password(self):
		return {
			"id": 123,
			"username": self._random_username(),
			"password": "short"
		}

	def invalid_user_no_password(self):
		return {
			"id": 123,
			"username": self._random_username()
		}

		

	def _random_username(self):
		return "user_"+"".join(random.choices(string.ascii_letters,k=5))
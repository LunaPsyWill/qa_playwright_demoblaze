import requests
import json

class APIClient:
	def __init__(self,base_url,timeout=10):
		self.base_url = base_url
		self.timeout = timeout
		self.session = requests.Session()

	def request(self,method,endpoint,**kwargs):
		url = f"{self.base_url}{endpoint}"

		response = self.session.request(
			method = method,
			url = url,
			timeout = self.timeout,
			**kwargs
			)

		if not response.ok:
			raise Exception(f"Request failed: {response.status_code} - {response.text}")

		return response

	def get(self,endpoint,**kwargs):
		response = self.request("GET",endpoint,**kwargs)

		return response

	def post(self,endpoint,**kwargs):
		response = self.request("POST",endpoint,**kwargs)

		return response

	def put(self,endpoint,**kwargs):
		return self.request("PUT",endpoint,**kwargs)

	def delete(self,endpoint):
		return self.request("DELETE",endpoint)
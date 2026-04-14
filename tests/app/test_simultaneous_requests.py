from app.api.endpoints import USERS
from app.models import User

def make_request(client,payload):
	return client.post(USERS,json=payload)

def test_simultaneous_requests(client,db):
	payload1 = {"name":"Carlos","email":"carlos@test.com"}
	payload2 = {"name":"Juan","email":"carlos@test.com"}

	responses = []

	def target(payload):
		res = make_request(client,payload)
		responses.append(res)
		return res

	r1 = target(payload1)
	r2 = target(payload2)

	success = [r for r in responses if r.status_code == 200]
	fail = [r for r in responses if r.status_code != 200]

	assert len(success) == 1
	assert len(fail) == 1

	user = db.query(User).filter(User.email == payload1["email"]).all()
	assert len(user) == 1
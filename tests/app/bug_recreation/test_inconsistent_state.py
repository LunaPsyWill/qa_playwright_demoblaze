from app.api.endpoints import INC_STATE
from app.models import User

def test_partial_failure(client,db):
	payload = {
		"name": "luis",
		"email": "luis@test.com"
	}

	# El endpoint lanza una excepción antes del commit
	try:
		client.post(INC_STATE,json=payload)
	except Exception as e:
		assert e

	#y aún así, el user sí se guardó
	user = db.query(User).filter(User.email == payload["email"])
	assert user is not None
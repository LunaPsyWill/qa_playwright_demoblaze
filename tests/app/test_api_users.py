from app.api.endpoints import USERS
from app.models import User

def test_create_user(client,db):
	payload = {
		"name": "Carlos",
		"email": "carlos@test.com"
	}

	response = client.post(
		USERS,
		json=payload
		)

	assert response.status_code ==  200

	user = db.query(User).filter(User.email == payload["email"]).first()

	assert user is not None
	assert user.name == "Carlos"
	assert user.email == "carlos@test.com"
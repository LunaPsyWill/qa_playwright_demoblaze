from app.models import User

def test_user_created_even_on_error(client,db):
	payload = {
		"name": "Carlos",
		"email": "carlos@test.com"
	}

	response = client.post("/users_bug",json=payload)
	assert response.status_code != 200

	user_exists = db.query(User).filter(User.email == payload["email"]).first()
	assert user_exists is not None
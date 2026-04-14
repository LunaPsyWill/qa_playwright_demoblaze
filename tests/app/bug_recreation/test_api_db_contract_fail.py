from app.api.endpoints import CONTRACT
from app.models import User

def test_api_db_contract(client,db):
	payload = {
		"name": "Ana",
		"email": "ana@test.com"
	}

	#desde el endpoint, devuelve un json con otros datos
	response = client.post(CONTRACT,json=payload)
	assert response.status_code == 200
	data = response.json()

	# #por lo que al validar los datos, no se mantiene la integridad
	user = db.query(User).filter(User.name == payload["name"]).first()
	assert data["email"] != user.email
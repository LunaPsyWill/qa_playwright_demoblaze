import pytest
import sqlite3
from fastapi import HTTPException
from app.api.endpoints import USERS

def test_duplicate_email(client):
	payload = {
		"name": "Ana",
		"email": "ana@test.com"
	}

	#primera request
	r1 = client.post(USERS,json=payload)
	assert r1.status_code == 200

	#se hace segunda request
	#se espera una exception
	r2 = client.post(USERS,json=payload)
	assert r2.status_code != 200
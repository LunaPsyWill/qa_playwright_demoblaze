import pytest
from database import create_connection,initialize_db
from mock_backend.repositories.user_repository import UserRepository


@pytest.fixture
def db():
	conn = create_connection()
	initialize_db(conn)

	yield conn
	conn.close()

@pytest.fixture
def repo(db):
	repo = UserRepository(db)
	return repo
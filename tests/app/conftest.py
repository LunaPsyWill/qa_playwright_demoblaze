import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient
from app.db import Base,get_db
from app.models import User
from app.main import app
from app.repositories.user_repository import UserRepository

SQLALCHEMY_DB_URL = "sqlite://"

engine = create_engine(SQLALCHEMY_DB_URL,connect_args={"check_same_thread":False},poolclass=StaticPool)
TestingSessionLocal = sessionmaker(bind=engine)

@pytest.fixture
def db():
	Base.metadata.create_all(bind=engine)
	session = TestingSessionLocal()
	yield session

	session.close()
	Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client(db):
	def override_get_db():
		session = TestingSessionLocal()
		try:
			yield db
		finally:
			pass

	app.dependency_overrides[get_db] = override_get_db

	yield TestClient(app)

	app.dependency_overrides.clear()

@pytest.fixture
def repo():
	repo = UserRepository()
	return repo

# import pytest
# from fastapi.testclient import TestClient
# from app.db import get_connection,init_db
# from app.main import app,get_db
# from app.repositories.user_repository import UserRepository

# @pytest.fixture
# def db():
# 	conn = get_connection(":memory:")
# 	init_db(conn)

# 	yield conn
# 	conn.close()

# @pytest.fixture
# def client(db):
# 	def override_get_db():
# 		return db

# 	app.dependency_overrides[get_db] = override_get_db

# 	return TestClient(app)

# @pytest.fixture
# def repo(db):
# 	repo = UserRepository(db)
# 	return repo
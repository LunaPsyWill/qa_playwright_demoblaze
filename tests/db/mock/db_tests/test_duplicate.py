from mock_backend.factories.db.db_factory import create_user
from mock_backend.repositories.user_repository import UserRepository

def test_no_duplicate_emails(db,repo):
	create_user(db,"Ana","anatest.com")
	
	cursor = db.cursor()

	result = repo.get_duplicated_emails()

	assert result == []


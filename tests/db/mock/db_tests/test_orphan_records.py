from mock_backend.factories.db.db_factory import create_order
from mock_backend.repositories.user_repository import UserRepository

def test_no_orphan_orders(db,repo):
	create_order(db,99,100)

	cursor = db.cursor()

	orphan = repo.get_orphan_orders()

	assert orphan != []

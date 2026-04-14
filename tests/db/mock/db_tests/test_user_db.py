from mock_backend.factories.db.db_factory import create_user,create_order
from mock_backend.repositories.user_repository import UserRepository

def test_user_db(db,repo):
	id_user = create_user(db,"Rick","rick@test.com")
	order_id = create_order(db,id_user,50)

	cursor = db.cursor()

	result = repo.get_orders_total(id_user)

	assert result == 50
import random
import string

def random_email():
	name = "".join(random.choices(string.ascii_lowercase,k=6))
	return f"{name}@test.com"

def create_user(db,name="User",email=None):
	if email is None:
		email = random_email()

	with db:
		cursor = db.cursor()

		cursor.execute(
			"INSERT INTO users(name,email) VALUES(?,?)",(name,email)
			)

		db.commit()
		return cursor.lastrowid

def create_order(db,user_id,total=100):
	with db:
		cursor = db.cursor()

		cursor.execute(
			"INSERT INTO orders(user_id,total) VALUES(?,?)",(user_id,total)
			)

		db.commit()
		return cursor.lastrowid
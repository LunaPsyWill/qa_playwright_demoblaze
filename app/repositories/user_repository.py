from sqlalchemy.orm import Session
from app.models import User

class UserRepository:
	def create_user(self,db:Session,name:str,email:str) -> User:
		user = User(name=name,email=email)
		db.add(user)
		db.commit()
		db.refresh(user)
		return user

	def create_user_not_persist(self,db:Session,name:str,email:str) -> User:
		user = User(name=name,email=email)
		db.add(user)
		# db.commit() #falta commit
		# db.refresh(user)
		return user

	def create_fail_contract(self,db:Session,name:str,email:str) -> User:
		user = User(name=name,email=email)
		db.add(user)
		db.commit()
		db.refresh(user)
		return user

	def get_user_by_email(self,db:Session,email:str) -> User | None:
		return db.query(User).filter(User.email == email).first()

	def get_users_by_email(self,db:Session,email:str) -> User | None:
		return db.query(User).filter(User.email == email).all()

	# def get_user_by_email(self,email):
	# 	self.cursor.execute(
	# 		"SELECT name,email FROM users WHERE email=?",(email,)
	# 		)

	# 	return self.cursor.fetchone()

	# def get_users_by_email(self,email):
	# 	self.cursor.execute(
	# 		"SELECT * FROM users WHERE email=?",(email,)
	# 		)

	# 	return self.cursor.fetchall()

	# def get_orders_total(self,id_user:int):
	# 	self.cursor.execute(
	# 		"SELECT total FROM orders WHERE user_id = ?",(id_user,)
	# 		)

	# 	return self.cursor.fetchone()[0]

	# def get_orphan_orders(self):
	# 	self.cursor.execute("""
	# 		SELECT o.id
	# 		FROM orders o
	# 		LEFT JOIN users u
	# 		ON o.user_id = u.id
	# 		WHERE u.id IS NULL"""
	# 		)

	# 	return self.cursor.fetchall()

	# def get_duplicated_emails(self):
	# 	self.cursor.execute("""
	# 		SELECT email
	# 		FROM users
	# 		GROUP BY email
	# 		HAVING COUNT(*) > 1
	# 		""")

	# 	return self.cursor.fetchall()
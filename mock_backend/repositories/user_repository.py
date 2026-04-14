import sqlite3

class UserRepository:
	def __init__(self,db):
		self.db = db
		self.cursor = self.db.cursor()

	def get_orders_total(self,id_user:int):
		self.cursor.execute(
			"SELECT total FROM orders WHERE user_id = ?",(id_user,)
			)

		return self.cursor.fetchone()[0]

	def get_orphan_orders(self):
		self.cursor.execute("""
			SELECT o.id
			FROM orders o
			LEFT JOIN users u
			ON o.user_id = u.id
			WHERE u.id IS NULL"""
			)

		return self.cursor.fetchall()

	def get_duplicated_emails(self):
		self.cursor.execute("""
			SELECT email
			FROM users
			GROUP BY email
			HAVING COUNT(*) > 1
			""")

		return self.cursor.fetchall()
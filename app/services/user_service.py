from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError,InvalidRequestError
from app.repositories.user_repository import UserRepository
from app.schemas import UserCreate

class UserService:
	def __init__(self):
		self.repo = UserRepository()

	def create_user(self,db:Session,user:UserCreate):
		try:
			return self.repo.create_user(db,user.name,user.email)
		except IntegrityError:
			db.rollback()
			raise HTTPException(status_code=409,detail="Email already exists")

		# existing_user = self.get_user(db,user)

		# if existing_user:
		# 	raise HTTPException(status_code=409,detail="Email already exists")

	def create_user_fail(self,db:Session,user:UserCreate):
		self.repo.create_user(db,user.name,user.email)
		raise HTTPException(status_code=500,detail="Something Failed")
		return user

	def create_user_inconsistent(self,db:Session,user:UserCreate):
		return self.repo.create_user_not_persist(db,user.name,user.email)
		
	def create_fail_contract(self,db:Session,user:UserCreate):
		user = self.repo.create_fail_contract(db,user.name,user.email)
		return {"name":user.name,"email":"fake@test.com"}

	def get_user(self,db:Session,user:UserCreate):
		return self.repo.get_user_by_email(db,user.email)

	# def get_user(self,user_id):
	# 	response = self.client.get(f"{USERS}{user_id}")

	# 	data = response.json()

	# 	if data.get("data"):
	# 		return response
		
	# 	if not data.get("password"):
	# 		raise KeyError("No password")

	# 	return response

	# def register_user(self,payload):
	# 	response = self.client.post(USERS,json=payload)

	# 	data = response.json()

	# 	if not data.get("data") and data.get("username") and data.get("password"):
	# 		return response

	# 	if not data["data"].get("password"):
	# 		raise KeyError("password does not exist")

	# 	if not data.get("created"):
	# 		raise ValueError("user not created")

	# 	return response
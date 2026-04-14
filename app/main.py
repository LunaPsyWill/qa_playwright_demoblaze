from fastapi import FastAPI,Depends
from app.schemas import UserCreate,UserResponse
from sqlalchemy.orm import Session
from app.db import get_db
from app.services.user_service import UserService
from app.api.endpoints import USERS,UNP,INC_STATE,CONTRACT
from fastapi import HTTPException

app = FastAPI()
user_service = UserService()

@app.post(USERS,response_model=UserResponse)
def create_user(user:UserCreate,db:Session = Depends(get_db)):
	return user_service.create_user(db,user)

#Endpoint para test_user_created_even_on_error
@app.post("/users_bug")
def create_user(user:UserCreate,db=Depends(get_db)):
	return user_service.create_user_fail(db,user)
	
@app.post(INC_STATE)
def inconsistent_state(user:UserCreate,db=Depends(get_db)):
	user_service.create_user_inconsistent(db,user)

	raise Exception("Something failed")

# Endpoint para test_api_db_contract
@app.post(CONTRACT)
def contract(user:UserCreate,db=Depends(get_db)):
	return user_service.create_fail_contract(db,user)
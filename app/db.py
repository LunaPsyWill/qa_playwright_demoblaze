from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker,Session

# def get_path(filename:str="") -> Path:
# 	return Path(__file__).resolve().parent / filename

engine = create_engine("sqlite:///test.db",echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
	db = SessionLocal()
	
	try:
		yield db
	finally:
		db.close()

# import sqlite3
# from pathlib import Path

# def get_path(filename:str="") -> Path:
# 	return Path(__file__).resolve().parent / filename

# def get_connection(filename:str):
# 	conn = sqlite3.connect(get_path(filename),
# 		check_same_thread=False,
# 		isolation_level=None,
# 		autocommit=False) if filename!=":memory:" else sqlite3.connect(filename,check_same_thread=False,isolation_level=None,autocommit=False)
	
# 	return conn

# def init_db(conn):
# 	file_path = get_path("schema.sql")
# 	with open(file_path) as f:
# 		conn.executescript(f.read())
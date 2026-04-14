import sqlite3
from pathlib import Path

def get_schema_path(filename:str) -> Path:
	return Path(__file__).resolve().parents[3] / "mock_backend" / "schemas" / filename

def create_connection():
	conn = sqlite3.connect(":memory:")
	return conn

def initialize_db(conn):
	sql_path = get_schema_path("db_user_order_schema.sql")
	with open(sql_path) as f:
		conn.executescript(f.read())
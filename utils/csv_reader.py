import csv
from pathlib import Path

def get_data_path(filename:str) -> Path:
	return Path(__file__).resolve().parents[1] / "data" / filename

def read_csv_users():
	csv_path = get_data_path("usuarios.csv")
	data = []
	with open(csv_path,newline="",encoding="utf-8") as file:
		reader = csv.DictReader(file)

		for row in reader:
			data.append((row["username"],row["password"],row["debe_pasar"]))

	return data

def read_csv_prods():
	csv_path = get_data_path("productos.csv")
	data = []
	with open(csv_path,newline="",encoding="utf-8") as file:
		reader = csv.DictReader(file)

		for row in reader:
			data.append((row["prod1"],row["prod2"]))

	return data

def read_csv_data():
	csv_path = get_data_path("datos_form.csv")
	data = []
	with open(csv_path,newline="",encoding="utf-8") as file:
		reader = csv.DictReader(file)

		for row in reader:
			data.append((row["name"],row["country"],row["city"],row["card"],row["month"],row["year"]))

	return data
import csv

def read_csv_users():
	data = []
	with open("data/usuarios.csv",newline="",encoding="utf-8") as file:
		reader = csv.DictReader(file)

		for row in reader:
			data.append((row["username"],row["password"],row["debe_pasar"]))

	return data

def read_csv_prods():
	data = []
	with open("data/productos.csv",newline="",encoding="utf-8") as file:
		reader = csv.DictReader(file)

		for row in reader:
			data.append((row["prod1"],row["prod2"]))

	return data

def read_csv_data():
	data = []
	with open("data/datos_form.csv",newline="",encoding="utf-8") as file:
		reader = csv.DictReader(file)

		for row in reader:
			data.append((row["name"],row["country"],row["city"],row["card"],row["month"],row["year"]))

	return data
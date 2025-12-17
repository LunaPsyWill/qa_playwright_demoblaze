import logging
import os
from datetime import datetime

def get_test_logger(test_name:str):
	os.makedirs("logs/tests",exist_ok=True)

	fecha1 = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
	fecha2 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	logger = logging.getLogger(f"{test_name}_logger")
	logger.setLevel(logging.INFO)

	log_filename = f"logs/tests/{test_name}_{fecha1}.log"
	fh = logging.FileHandler(log_filename,mode="w",encoding="utf-8")
	fh.setLevel(logging.INFO)

	formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s",fecha2)
	fh.setFormatter(formatter)

	if not logger.handlers:
		logger.addHandler(fh)

	return logger

def get_class_logger(class_name:str):
	log_dir = "logs/class"
	os.makedirs(log_dir,exist_ok=True)

	fecha = datetime.now().strftime('%Y-%m-%d')
	logger = logging.getLogger(class_name)
	logger.setLevel(logging.INFO)
	logger.propagate = False		

	handler = logging.FileHandler(f"{log_dir}/{class_name}_{fecha}.log",mode="a",encoding="utf-8")
	formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s")
	handler.setFormatter(formatter)

	if not logger.handlers:
		logger.addHandler(handler)

		for handler in logger.handlers:
			if hasattr(handler,"stream"):
				handler.stream.write("\n")
				handler.stream.flush()

	return logger
import logging
import os
from datetime import datetime
from pathlib import Path

def get_logs_path(_dir:str,filename:str = "") -> Path:
	return Path(__file__).resolve().parents[1] / "logs" / _dir / filename

def get_test_logger(test_name:str):
	os.makedirs(get_logs_path("tests"),exist_ok=True)

	fecha1 = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
	fecha2 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	logger = logging.getLogger(f"{test_name}_logger")
	logger.setLevel(logging.INFO)

	log_filename = get_logs_path("tests",f"{test_name}_{fecha1}.log") 
	fh = logging.FileHandler(log_filename,mode="w",encoding="utf-8")
	fh.setLevel(logging.INFO)

	formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s",fecha2)
	fh.setFormatter(formatter)

	if not logger.handlers:
		logger.addHandler(fh)

	return logger

def get_class_logger(class_name:str):
	os.makedirs(get_logs_path("class"),exist_ok=True)

	fecha = datetime.now().strftime('%Y-%m-%d')
	logger = logging.getLogger(class_name)
	logger.setLevel(logging.INFO)
	logger.propagate = False		

	log_filename = get_logs_path("class",f"{class_name}_{fecha}.log")
	handler = logging.FileHandler(log_filename,mode="a",encoding="utf-8")
	formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s")
	handler.setFormatter(formatter)

	if not logger.handlers:
		logger.addHandler(handler)

		for handler in logger.handlers:
			if hasattr(handler,"stream"):
				handler.stream.write("\n")
				handler.stream.flush()

	return logger
import allure
import logging
import os
import json
from playwright.sync_api import Page,TimeoutError as PlaywrightTimeoutError
from utils.logger import get_class_logger

class BasePage:
	def __init__(self,page:Page,timeout:int = 6000):
		self.page = page
		self.timeout = timeout

		#===== Logger profesional por clase =====
		self.logger = get_class_logger(self.__class__.__name__)

	#===== MÉTODOS DE ALLURE =====
	def step(self,description:str):
		return allure.step(description)

	def attach(self,type:str,nombre:str,adj:list = []):
		if type.lower()=="scr" or type.lower()=="screenshot":
			allure.attach(self.page.screenshot(),name=nombre,attachment_type=allure.attachment_type.PNG)
		elif type.lower()=="json":
			allure.attach(json.dumps(adj,indent=2),name=nombre,attachment_type=allure.attachment_type.JSON)
		elif type.lower()=="html":
			allure.attach(self.page.content(),name=nombre,attachment_type=allure.attachment_type.HTML)

	#===== MÉTODOS DE ESPERA =====
	def wait_for_visible(self,selector:str):
		try:
			self.page.wait_for_selector(selector,state="visible")
			self.logger.info(f"Visible: {selector}")

		except PlaywrightTimeoutError:
			self._fail(f"No apareció el selector: {selector}")

	def wait_first_visible(self,selector:str):
		try:
			self.page.locator(selector).first.wait_for(state="visible")
			self.logger.info(f"First visible: {selector}")

		except PlaywrightTimeoutError:
			self._fail(f"No apareció el primer elemento: {selector}")

	#===== MÉTODOS DE INTERACCIÓN =====
	def click(self,selector:str):
		self.wait_for_visible(selector)
		try:
			self.page.click(selector)
			self.logger.info(f"Click en {selector}")

		except Exception as e:
			self._fail(f"Error al hacer click en {selector}: {e}")

	def fill(self,selector:str,text:str):
		self.wait_for_visible(selector)
		try:
			self.page.fill(selector,text)
			self.logger.info(f"Fill en {selector} con {text}")

		except Exception as e:
			self._fail(f"Error al hacer fill en {selector}: {e}")

	#===== MÉTODOS DE LECTURA =====
	def get_text(self,selector:str) -> str:
		self.wait_for_visible(selector)
		try:
			txt = self.page.locator(selector).inner_text().strip()
			self.logger.info(f"Texto leído en {selector}: {txt}")
			return txt
		except Exception as e:
			self._fail(f"Error al obtener texto de {selector}: {e}")
	
	# def assert_text(self,selector:str,expected:str):
	# 	expect(self.page.locator(selector)).to_have_text(expected)

	def get_all_texts(self,selector:str) -> list:
		self.wait_for_visible(selector)
		try:
			textos = [t.strip() for t in self.page.locator(selector).all_inner_texts()]
			self.logger.info(f"Textos leídos en {selector}: {textos}")
			return textos
		except Exception as e:
			self._fail(f"Error al obtener textos múltiples de {selector}: {e}")

	#===== ASSERTS PROFESIONALES =====
	def verify(self,condition:bool,message_err:str,message_ok:str = "Verificación correcta."):
		#assert con screenshot + log + adjunto Allure
		with allure.step(f"Verificación de: {message_ok}"):
			if not condition:
				self._fail(message_err)
				assert False
			else:
				self.logger.info(f"Verificación OK: {message_ok}")
				self.attach("scr","Screenshot Verificación OK")
				assert True

	#===== MÉTODO CENTRAL DE ERROR =====
	def _fail(self,message:str):
		self.logger.error(message)
		screenshot = self.page.screenshot()
		self.attach("scr","Screenshot de error")
		raise AssertionError(message)
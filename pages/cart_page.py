import json
import allure
from pages.base_page import BasePage

class CartPage(BasePage):
	def ir_al_carrito(self):
		with self.step("Ir al carrito."):
			self.click("#cartur")

	def verificar_redir_carrito(self):
		with self.step("Verificando redirección al carrito."):
			self.verify("cart" in self.page.url, 
				"La redirección al carrito no es correcta.",
				"Redirección al carrito correcta.")

	def obtener_productos(self):
		self.wait_first_visible("tr.success")
		nombres = self.page.locator("tr.success td:nth-child(2)").all_inner_texts()

		self.attach("json","Productos encontrados en carrito.",nombres)

		return [n.strip() for n in nombres]

	def verificar_productos(self,productos_esperados):
		with self.step("Verificando productos en carrito."):
			nombres = self.obtener_productos()
			for p in productos_esperados:
				self.verify(p in nombres, 
					f"El producto {p} no está en el carrito.",
					f"ÉXITO: producto '{p}' en carrito.")

	def obtener_precios(self):
		with self.step("Obtener precios."):
			self.wait_first_visible("tr.success")
			precios = self.page.locator("tr.success td:nth-child(3)").all_inner_texts()
			return [int(p) for p in precios]

	def obtener_total(self):
		with self.step("Obtener total."):
			total = self.page.locator("#totalp").text_content()
			return int(total.strip())

	def click_place_order(self):
		with self.step("Click en Place Order."):
			self.click("button[data-target='#orderModal']")
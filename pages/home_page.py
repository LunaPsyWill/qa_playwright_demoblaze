from pages.base_page import BasePage

class HomePage(BasePage):
	def seleccionar_producto(self,nombre_producto):
		self.page.click(f"text={nombre_producto}")

	def agregar_al_carrito(self):
		with self.page.expect_event("dialog") as dlg:
			self.click("text=Add to cart")
			dlg.value.accept()

	def volver_al_home(self):
		self.click(".navbar-brand")

	def seleccionar_agregar_volver(self,productos):
		with self.step(f"Agregando productos."):
			for p in productos:
				self.seleccionar_producto(p)
				self.agregar_al_carrito()
				self.volver_al_home()
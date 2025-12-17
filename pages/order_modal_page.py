from pages.base_page import BasePage

class OrderModalPage(BasePage):
	def esperar_modal_visible(self):
		with self.step("Esperando modal visible."):
			self.wait_for_visible("#orderModal")

	def llenar_formulario(self,datos):
		with self.step("Llenando formulario."):
			id_list = ['name','country','city','card','month','year']

			for nombre,valor in zip(id_list,datos):
				self.fill(f"#{nombre}",valor)

	def click_purchase(self):
		with self.step("Click en purchase."):
			self.click("#orderModal .btn-primary")
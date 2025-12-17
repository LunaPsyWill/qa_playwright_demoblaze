from pages.base_page import BasePage

class ConfirmPurchasePage(BasePage):
	def esperar_confirmacion_visible(self):
		with self.step("Esperar confirmación visible."):
			self.wait_for_visible("div.sweet-alert.showSweetAlert.visible")

	def extraer_datos_finales(self):
		with self.step("Extraer datos finales."):
			datos = self.page.locator("p.lead.text-muted").inner_text()

			self.attach("html","Estado del DOM")

			return datos.split('\n')

	def validar_monto(self,precios):
		with self.step("Validar monto final."):
			suma = sum(precios)
			datosf = self.extraer_datos_finales()
			amount = int(datosf[1].split()[1])

			self.verify(amount == suma,
				"El total no coincide con la suma de precios.",
				"El total es correcto.")

	def validar_mensaje(self):
		with self.step("Validar mensaje final."):
			mensaje = self.page.locator("div.sweet-alert.showSweetAlert.visible h2").inner_text()
			
			self.verify("thank you" in mensaje.lower(),
				"El modal no contiene mensaje de agradecimiento.",
				"Modal con mensaje de confirmación correcto.")

	def cerrar_modal(self):
		with self.step("Cerrando modal."):
			self.click(".confirm.btn.btn-lg.btn-primary")
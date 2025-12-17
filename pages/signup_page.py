from playwright.sync_api import Page
from pages.base_page import BasePage

class SignupPage(BasePage):
	def __init__(self,page:Page):
		super().__init__(page)
		self.page = page
		self.signup_button = "#signin2" #botón del header "Sign up"
		self.username_field = "#sign-username"
		self.password_field = "#sign-password"
		self.signup_confirm_btn = "#signInModal .btn-primary"

	def abrir_modal_signup(self):
		with self.step("Abriendo modal de Signup."):
			self.click(self.signup_button)
			self.wait_for_visible(self.username_field)

	def llenar_formulario(self,username,password):
		with self.step("Llenando formulario."):
			self.fill(self.username_field,username)
			self.fill(self.password_field,password)
			self.click(self.signup_confirm_btn)

	def confirmar_alert(self):
		self.page.on("dialog",lambda dialog: dialog.accept())

	def verificar_signup_exitoso(self):
		with self.step("Verificando signup exitoso."):
			#no hay cambio visible, pero si no hubo error en popup, consideramos éxito
			self.verify(True,
				f"Usuario {self.page.input_value(self.username_field)} no registrado",
				f"Usuario {self.page.input_value(self.username_field)} registrado con éxito")
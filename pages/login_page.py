from pages.base_page import BasePage


class LoginPage(BasePage):
	def __init__(self,page):
		super().__init__(page)
		self.page = page
		self.login_button = "#login2"
		self.username_field = "#loginusername"
		self.password_field = "#loginpassword"
		self.confirm_login_btn = "#logInModal .btn-primary"
		self.logout_btn = "#logout2"

	def abrir_modal_login(self):
		with self.step("Abrir modal del login."):
			self.click(self.login_button)
			self.wait_for_visible("#logInModal")

	def llenar_datos(self,username,password):
		with self.step("Llenar datos del formulario."):
			self.fill(self.username_field,username)
			self.fill(self.password_field,password)
			self.click(self.confirm_login_btn)

	def verificar_login_exitoso(self,username):
		with self.step("verificar login exitoso."):
			self.wait_for_visible("#nameofuser")
			nombre = self.get_text("#nameofuser")

			self.verify(username in nombre, 
				f"El login falló, se esperaba {username}",
				f"Login Exitoso, se muestra el nombre correcto: {username}")
import pytest
from utils.csv_reader import read_csv_users
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.order_modal_page import OrderModalPage
from pages.confirm_purchase_page import ConfirmPurchasePage
import random,string

@pytest.fixture
def generar_usuario():
	letras = string.ascii_lowercase
	username = "user_" + ''.join(random.choice(letras) for _ in range(5))
	password = ''.join(random.choice(letras) for _ in range(8))
	return username,password

@pytest.fixture
def signup(page,test_logger,generar_usuario):
	def do_signup():
		username,password = generar_usuario
		signup = SignupPage(page)
		test_logger.info("Iniciando Signup")
		signup.abrir_modal_signup()
		signup.llenar_formulario(username,password)
		signup.confirmar_alert()
		signup.verificar_signup_exitoso()
		test_logger.info("Signup correcto")

		return [username,password]
	return do_signup

@pytest.fixture
def usuario_valido():
	users = read_csv_users()
	valido = []
	for user in users:
		valido.append(user) if user[2]=="TRUE" else None
	return valido[0]

@pytest.fixture
def login(page,test_logger,usuario_valido,signup):
	def _global():
		username,password,_ = usuario_valido
		login = LoginPage(page)
		test_logger.info("Iniciando Login")
		login.abrir_modal_login()
		login.llenar_datos(username,password)
		login.verificar_login_exitoso(username)
		test_logger.info("Login Correcto")

	def signup_login():
		username,password = signup()
		login = LoginPage(page)
		test_logger.info("Iniciando Login")
		login.abrir_modal_login()
		login.llenar_datos(username,password)
		login.verificar_login_exitoso(username)
		test_logger.info("Login Correcto")

	def ejecutar(modo=None):
		if modo == "signup":
			return signup_login()
		else:
			return _global()

	return ejecutar

@pytest.fixture
def paginas(page):
	home = HomePage(page)
	cart = CartPage(page)
	omodal = OrderModalPage(page)
	confirm = ConfirmPurchasePage(page)

	return [home,cart,omodal,confirm]

@pytest.fixture
def flujo_compra(page,test_logger,login,paginas):
	def ejecutar(prods,datos):
		home,cart,omodal,confirm = paginas
		#-----PRODUCTOS-----
		test_logger.info(f"Agregando productos: {prods}")
		home.seleccionar_agregar_volver(prods)

		#-----CARRITO-----
		test_logger.info("Verificando productos en carrito.")
		cart.ir_al_carrito()
		cart.verificar_redir_carrito()
		cart.verificar_productos(prods)
		test_logger.info("Productos verificados en carrito.")

		precios = cart.obtener_precios()
		test_logger.info(f"Precios encontrados: {precios}")

		cart.click_place_order()

		#-----PLACE ORDER-----
		omodal.esperar_modal_visible()

		omodal.llenar_formulario(datos)
		omodal.click_purchase()
		test_logger.info("Formulario enviado y compra realizada.")

		#-----CONFIRMACIÓN-----
		confirm.esperar_confirmacion_visible()
		confirm.validar_monto(precios)
		confirm.validar_mensaje()
		test_logger.info("Compra confirmada.")

		confirm.cerrar_modal()
		test_logger.info("Test completado.")

	return ejecutar
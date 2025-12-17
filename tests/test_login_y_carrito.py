import pytest
import allure
from utils.csv_reader import read_csv_prods
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage

@pytest.mark.parametrize("prods",read_csv_prods())

@allure.feature("Productos en Carrito.")
@allure.story("Flujo hasta verificar productos en carrito")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.functional
@pytest.mark.integration
def test_login_y_carrito(test_logger,login,paginas,prods):
	home,cart,_,_ = paginas

	#-----PRODUCTOS-----
	test_logger.info(f"Agregando productos: {prods}")
	home.seleccionar_agregar_volver(prods)

	#-----CARRITO-----
	test_logger.info("Verificando productos en carrito.")
	cart.ir_al_carrito()
	cart.verificar_redir_carrito()
	cart.verificar_productos(prods)
import pytest
import allure
from pages.login_page import LoginPage

@allure.feature("Signup")
@allure.story("Registrar usuario y hacer Login")
@pytest.mark.functional
@pytest.mark.integration
@pytest.mark.signup
@pytest.mark.login
def test_signup_login(login):
	login("signup")
import pytest
import allure
from utils.csv_reader import read_csv_prods
from utils.csv_reader import read_csv_data

@pytest.mark.parametrize("prods,datos",zip(read_csv_prods(),read_csv_data()))

@allure.feature("compra")
@allure.story("Flujo completo de compra")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.functional
@pytest.mark.integration
@pytest.mark.e2e
def test_compra(flujo_compra,prods,datos):
	flujo_compra(prods,datos)
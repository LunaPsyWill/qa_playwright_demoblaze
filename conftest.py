import pytest
import os
from dotenv import load_dotenv
from utils.logger import get_test_logger

load_dotenv()

# def pytest_addoption(parser):
# 	parser.addoption(
# 		"--env",
# 		action="store",
# 		default="dev",
# 		help="Environment to tun tests against"
# 		)

@pytest.fixture
def test_logger(request):
	test_name = request.node.name
	logger = get_test_logger(test_name)
	logger.info(f"===== INICIANDO TEST: {test_name} =====")
	yield logger
	logger.info(f"===== FINALIZANDO TEST: {test_name} =====")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
	outcome = yield
	result = outcome.get_result()

	if result.when == "call" and result.failed:
		page = item.funcargs.get("page",None)
		if page:
			#screenshot del fallo
			allure.attach(page.screenshot(),
				name="Error screenshot",
				attachment_type=allure.attachment_type.PNG)

			#HTML del DOM
			html = page.content()
			allure.attach(html,
				name="DOM HTML",
				attachment_type=allure.attachment_type.HTML)
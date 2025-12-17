import pytest
import allure
import os
from playwright.sync_api import sync_playwright
from utils.logger import get_test_logger

HEADLESS = True if os.getenv("CI") else False

@pytest.fixture(scope="function")
def page():
	with sync_playwright() as p:
		browser = p.chromium.launch(headless=HEADLESS,slow_mo=300)
		context = browser.new_context()
		page = context.new_page()
		page.goto("https://www.demoblaze.com/")
		yield page
		context.close()
		browser.close()

@pytest.fixture
def test_logger(request):
	test_name = request.node.name
	logger = get_test_logger(test_name)
	logger.info(f"===== INICIANDO TEST: {test_name} =====")
	yield logger
	logger.info(f"===== FINALIZANDO TEST: {test_name} =====")

@pytest.fixture(autouse=True)
def allure_setup(page):
	yield

	if hasattr(page,"is_closed") and not page.is_closed():
		try:
			screenshot = page.screenshot()
			allure.attach(screenshot,
				"Screenshot final",
				allure.attachment_type.PNG)
		except:
			pass

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
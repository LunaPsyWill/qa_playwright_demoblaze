# Automatización E2E de Demoblaze con Playwright + Pytest + Allure Report.

## Descripción.
Proyecto profesional de automatización QA basado en Playwright y Pytest.
Incluye POM, logging, asserts customizados, attachments (screenshots, json y html) y reportes Allure.

## Tecnologías.
- Playwright (Python)
- Pytest
- Allure Report
- Python Logging
- Patrón Page Object Model

## Cómo Ejecutar.
'''bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pytest --alluredir=allure-results
allure serve allure-results

## Arquitectura del proyecto.
/pages
/tests
/utils
conftest.py

## Qué contiene.
- (sólo si se desea) Signup automatizado.
- Login automatizado.
- Compra completa E2E.
- Assertions personalizados.
- Esperas inteligentes.
- Logs por página.
- Logs por test.
- Evidencias Allure.

## Ejemplo de reporte Allure.
![Allure Report](./images/allure_example.png)

## Qué aprendí.
Aprendí las bases de Playwright, el cual, a mi parecer, es un framework más eficiente que Selenium, ya que Playwright se ahorra métodos como driver.find_element(BY,"locator"), todo lo hace más fácil de escribir con los métodos que ya trae el objeto Page, como click, fill, goto, wait_for_selector, etc. Otra ventaja es el ahorrarse la declaración del webdriver según en navegador que se vaya a usar, Playwright ya lo trae integrado.
En general, es una bonita experiencia trabajar con este framework, dejando todo el código escrito de manera eficiente y elegante.
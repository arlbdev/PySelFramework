import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Command line options for running test in different browsers
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    service = Service()

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=service)
    elif browser_name == "edge":
        driver = webdriver.Edge(service=service)

    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    request.cls.driver = driver
    yield
    print("Testing completed. Please see the results.")
    driver.close()

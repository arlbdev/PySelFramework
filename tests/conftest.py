import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None

SCREENSHOT_DIR = "../reports"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Command line options for running test in different browsers
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    service = Service()
    global driver

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


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):

    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            file_path = os.path.join(SCREENSHOT_DIR, file_name)
            _capture_screenshot(file_path)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(file_path):
    driver.get_screenshot_as_file(file_path)

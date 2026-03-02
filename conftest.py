import os
import logging




import allure

from datetime import datetime

import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from utils.config_reader import config_reader


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser to use")

@pytest.fixture
def page(request):
    browser_name = request.config.getoption("--browser_name")
    headed = request.config.getoption("headed")
    headless = not headed
    config = config_reader()
    url = config["base_url"]
    with sync_playwright() as playwright:
        if browser_name == "chrome":
            browser = playwright.chromium.launch(headless=headless)
        elif browser_name == "firefox" :
            browser = playwright.firefox.launch(headless=headless)
        elif browser_name == "edge":
            browser = playwright.chromium.launch(channel="msedge", headless=headless)
        elif browser_name == "webkit":
            browser = playwright.webkit.launch(headless=headless)
        else:
            raise ValueError("Invalid browser name")
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        yield page
        page.close()
        context.close()
        browser.close()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page", None)

        if page:

            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"reports/screenshots/{item.name}_{timestamp}.png"

            # Capture screenshot
            page.screenshot(path=screenshot_path)

            # Attach screenshot to Allure
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        # Attach log file to Allure
        log_path = os.path.join(os.getcwd(), "reports", "logs", f"{item.name}.log")

        if os.path.exists(log_path):
            allure.attach.file(
                log_path,
                name="Execution Logs",
                attachment_type=allure.attachment_type.TEXT
            )







@pytest.fixture
def logger(request):

    test_name = request.node.name

    logs_dir = os.path.join(os.getcwd(), "reports", "logs")
    os.makedirs(logs_dir, exist_ok=True)

    log_file = os.path.join(logs_dir, f"{test_name}.log")

    logger = logging.getLogger(test_name)
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_file, mode="w")
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

@pytest.fixture(scope="function")
def log_in_to_page(page, logger):
    config = config_reader()
    username = config["username"]
    password = config["password"]
    login = LoginPage(page, logger)
    login.open_Login_page()
    login.enter_credentials(username, password)
    logger.info("Login successful")
    return login


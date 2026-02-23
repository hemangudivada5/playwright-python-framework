import os

import allure
import pytest
from datetime import datetime

import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser to use")

@pytest.mark.fixture
def browser_instance(request):
    browser_name = request.config.getoption("--browser_name")
    with sync_playwright() as playwright:
        if browser_name == "chrome":
            playwright.chromium.launch(headless=True)
        elif browser_name == "firefox" :
            playwright.firefox.launch(headless=True)
        elif browser_name == "edge":
            browser = playwright.chromium.launch(channel="msedge", headless=False)
        elif browser_name == "webkit":
            browser = playwright.webkit.launch(headless=True)
        else:
            raise ValueError("Invalid browser name")
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    browser.close()
    context.close()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page", None)

        if page:

            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"screenshots/{item.name}_{timestamp}.png"

            # Capture screenshot
            page.screenshot(path=screenshot_path)

            # Attach screenshot to Allure
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        # Attach log file to Allure
        log_path = "logs/test.log"

        if os.path.exists(log_path):
            allure.attach.file(
                log_path,
                name="Execution Logs",
                attachment_type=allure.attachment_type.TEXT
            )


from utils.config_reader import config_reader
from datetime import datetime

from playwright.sync_api import Playwright, expect

from utils.data_generator import generate_Email_Time_Stamp


def test_Verify_Register_Account_Functionality_By_Providing_All_Fields(page):
    config = config_reader()
    url = config["base_url"]
    page.goto(url)
    page.locator("//span[text()='My Account']").click()
    page.locator("//a[text()='Register']").click()
    page.get_by_placeholder("First Name").fill("hemanth")
    page.get_by_placeholder("Last Name").fill("Chand")
    page.get_by_placeholder("E-Mail").fill("hemanth"+generate_Email_Time_Stamp()+"@gmail.com")
    page.get_by_placeholder("Telephone").fill("1234567890")
    page.locator("//input[@id='input-password']").fill("Hemanth@1234")
    page.locator("//input[@id='input-confirm']").fill("Hemanth@1234")
    page.locator("//input[@name='newsletter' and @value=1]").click()
    page.locator("//input[@name='agree' and @value=1]").check()
    page.locator("//input[@type='submit']").click()

    expect(page.locator("body")).to_contain_text("Your Account Has Been Created!")



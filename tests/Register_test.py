from utils import logger
from utils.config_reader import config_reader
from datetime import datetime

from playwright.sync_api import Playwright, expect

from utils.data_generator import generate_Email_Time_Stamp


def test_Verify_Register_Account_Functionality_By_Providing_All_Fields(page, logger):
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


def test_verify_Register_Account_Functionality_with_existing_email(page, logger):
    page.locator("//span[text()='My Account']").click()
    page.locator("//a[text()='Register']").click()
    page.get_by_placeholder("First Name").fill("hemanth")
    page.get_by_placeholder("Last Name").fill("Chand")
    page.get_by_placeholder("E-Mail").fill("chandugudivada10@gmail.com")
    page.get_by_placeholder("Telephone").fill("1234567890")
    page.locator("//input[@id='input-password']").fill("Hemanth@1234")
    page.locator("//input[@id='input-confirm']").fill("Hemanth@1234")
    page.locator("//input[@name='newsletter' and @value=1]").click()
    page.locator("//input[@name='agree' and @value=1]").check()
    page.locator("//input[@type='submit']").click()
    expect(page.locator("//div[@class='alert alert-danger alert-dismissible']")).to_contain_text("Warning: E-Mail Address is already registered!")

def test_verify_Register_Account_Functionality_without_Data(page, logger):
    page.locator("//span[text()='My Account']").click()
    page.locator("//a[text()='Register']").click()
    page.locator("//input[@type='submit']").click()
    expect(page.locator("//div[@class='alert alert-danger alert-dismissible']")).to_contain_text("Warning: You must agree to the Privacy Policy!")
    expect(page.locator("//input[@id='input-firstname']/following-sibling::div")).to_contain_text("First Name must be between 1 and 32 characters!")
    expect(page.locator("//input[@id='input-lastname']/following-sibling::div")).to_contain_text("Last Name must be between 1 and 32 characters!")
    expect(page.locator("//input[@id='input-email']/following-sibling::div")).to_contain_text("E-Mail Address does not appear to be valid!")
    expect(page.locator("//input[@id='input-telephone']/following-sibling::div")).to_contain_text("Telephone must be between 3 and 32 characters!")
    expect(page.locator("//input[@id='input-password']/following-sibling::div")).to_contain_text("Password must be between 4 and 20 characters!")

def test_verify_Register_Option_In_Register_page_Works(page, logger):
    page.locator("//span[text()='My Account']").click()
    page.locator("//a[text()='Register']").click()
    page.locator("//a[@class='list-group-item' and text()='Register']").click()
    expect(page.locator("body")).to_contain_text("Your Personal Details")

def test_verify_Error_Msg_displayed_when_register_without_privacypolicy(page, logger):
    page.locator("//span[text()='My Account']").click()
    page.locator("//a[text()='Register']").click()
    page.get_by_placeholder("First Name").fill("hemanth")
    page.get_by_placeholder("Last Name").fill("Chand")
    page.get_by_placeholder("E-Mail").fill("chandugudivada10@gmail.com")
    page.get_by_placeholder("Telephone").fill("1234567890")
    page.locator("//input[@id='input-password']").fill("Hemanth@1234")
    page.locator("//input[@id='input-confirm']").fill("Hemanth@1234")
    page.locator("//input[@type='submit']").click()
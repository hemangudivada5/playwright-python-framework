from playwright.sync_api import Page

from pages.base_page import BasePage


class RegisterSuccessPage(BasePage):
    Account_Success_Text = "//div[@id='content']/h1"
    def verify_register_success_text(self):
        return self.get_text(self.Account_Success_Text)

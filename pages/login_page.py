from pages.base_page import BasePage


class LoginPage(BasePage):
    MY_ACCOUNT = "//span[text()='My Account']"
    Login_Option = "//a[text()='Login']"
    Email = "//input[@id='input-email']"
    Password = "//input[@id='input-password']"
    Login_Button = "//input[@value='Login']"
    Login_Verify_Text = "//a[text()='Edit your account information']"
    invalid_login_msg = "//div[text()='Warning: No match for E-Mail Address and/or Password.']"

    def open_Login_page(self):
        self.click(self.MY_ACCOUNT)
        self.click(self.Login_Option)

    def enter_credentials(self, Email_Text, Password_Text):
        self.fill(self.Email, Email_Text)
        self.fill(self.Password, Password_Text)
        self.click(self.Login_Button)

    def verify_Login_Success(self):
        return self.get_text(self.Login_Verify_Text)

    def Invalid_Login_Warning(self):
        return self.get_text(self.invalid_login_msg)
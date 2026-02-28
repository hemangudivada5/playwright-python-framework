from pages.login_page import LoginPage
from utils.config_reader import config_reader


def test_verify_Login_With_Valid_Credentials(page,logger):
    config = config_reader()
    Email_id = config["username"]
    Password = config["password"]
    login_page = LoginPage(page,logger)
    login_page.open_Login_page()
    login_page.enter_credentials(Email_id,Password)
    verify_Text = login_page.Login_Verify_Text
    assert "Edit your account information" in verify_Text

def test_verify_Login_With_Invalid_Credentials(page,logger):
    config = config_reader()
    invalid_Email_id = config["invalid_username"]
    invalid_Password = config["invalid_password"]
    login_page = LoginPage(page,logger)
    login_page.open_Login_page()
    login_page.enter_credentials(invalid_Email_id,invalid_Password)
    invalid_login_test = login_page.invalid_login_msg
    assert "Warning: No match for E-Mail Address and/or Password." in invalid_login_test


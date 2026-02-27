from pages.register_page import RegisterPage

from utils.data_generator import generate_Email_Time_Stamp



def test_Verify_Register_Account_Functionality_By_Providing_All_Fields(page, logger):
    Email_Text = "hemanth"+generate_Email_Time_Stamp()+"@gmail.com"
    register_Page = RegisterPage(page, logger)
    register_Page.open_register_page()
    register_Page.enter_user_details(
        "Hemanth",
        "Chand",
        Email_Text,
        "aabbccdd",
        "aabbccdd",
        "1234567890")
    success_Text = register_Page.verify_register_success_text()
    assert "Your Account Has Been Created!" in success_Text


def test_verify_Register_Account_Functionality_with_existing_email(page, logger):
    register_Page = RegisterPage(page, logger)
    register_Page.open_register_page()
    register_Page.enter_user_details(
        "Hemanth",
        "Chand",
        "chandugudivada10@gmail.com",
        "aabbccdd",
        "aabbccdd",
        "1234567890")
    Warning_Message_Text = register_Page.Duplicate_Email_Warning_Retrieval()
    assert "Warning: E-Mail Address is already registered!" in Warning_Message_Text


def test_verify_Register_Account_Functionality_without_Data(page, logger):
    register_Page = RegisterPage(page, logger)
    register_Page.open_register_page()
    register_Page.register_user_Without_Data()
    privacy_Warning_Text = register_Page.No_Privacy_Policy_Warning()
    assert "Warning: You must agree to the Privacy Policy!" in privacy_Warning_Text
    first_Name_Warning_Text = register_Page.No_First_Name_Warning()
    assert "First Name must be between 1 and 32 characters!" in first_Name_Warning_Text
    last_Name_Warning_Text = register_Page.No_Last_Name_Warning()
    assert "Last Name must be between 1 and 32 characters!" in last_Name_Warning_Text
    email_Warning_Text = register_Page.No_Email_Warning()
    assert "E-Mail Address does not appear to be valid!" in email_Warning_Text
    telephone_Warning_Text = register_Page.No_Telephone_Warning()
    assert "Telephone must be between 3 and 32 characters!" in telephone_Warning_Text
    password_Warning_Text = register_Page.No_Password_Warning()
    assert "Password must be between 4 and 20 characters!" in password_Warning_Text

def test_verify_Register_Option_In_Register_page_Works(page, logger):
    register_Page = RegisterPage(page, logger)
    register_Page.open_register_page()
    register_Page.Open_Register_Page_In_Register_Page()
    Personal_Details_Text = register_Page.Verify_Register_Page_From_Personal_Details_Message()
    assert "Your Personal Details" in Personal_Details_Text

def test_verify_Error_Msg_displayed_when_register_without_privacypolicy(page, logger):
    register_Page = RegisterPage(page, logger)
    register_Page.open_register_page()
    register_Page.Verify_Register_Without_Selecting_Private_Policy(
        "Hemanth",
        "Chand",
        "chandugudivada10@gmail.com",
        "aabbccdd",
        "aabbccdd",
        "1234567890")
    Private_Policy_Warning_Text = register_Page.No_Privacy_Policy_Warning()
    assert "Warning: You must agree to the Privacy Policy!" in Private_Policy_Warning_Text

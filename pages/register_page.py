from pages.base_page import BasePage


class RegisterPage(BasePage):
    MY_ACCOUNT = "//span[text()='My Account']"
    REGISTER_ACCOUNT = "//a[text()='Register']"
    FIRST_NAME = "//input[@id='input-firstname']"
    LAST_NAME = "//input[@id='input-lastname']"
    EMAIL = "//input[@id='input-email']"
    TELEPHONE = "//input[@id='input-telephone']"
    PASSWORD = "//input[@id='input-password']"
    PASSWORD_CONFIRM = "//input[@id='input-confirm']"
    NEWSLETTER = "//input[@name='newsletter' and @value='1']"
    PRIVACY_POLICY = "//input[@name='agree' and @value='1']"
    SUBMIT_BUTTON = "//input[@type='submit']"
    Account_Success_Text = "//div[@id='content']/h1"
    Duplicate_Email_Warning = "//div[@class='alert alert-danger alert-dismissible']"
    Privacy_Policy_Warning = "//div[@class='alert alert-danger alert-dismissible']"
    First_Name_Warning = "//input[@id='input-firstname']/following-sibling::div"
    Last_Name_Warning = "//input[@id='input-lastname']/following-sibling::div"
    EMail_Warning = "//input[@id='input-email']/following-sibling::div"
    Telephone_Warning = "//input[@id='input-telephone']/following-sibling::div"
    Password_Warning = "//input[@id='input-password']/following-sibling::div"
    Register_Option_In_Register_Page = "//a[@class='list-group-item' and text()='Register']"
    Personal_Details_Confirm_Text = "//fieldset[@id='account']//legend"

    def open_register_page(self):
        self.click(self.MY_ACCOUNT)
        self.click(self.REGISTER_ACCOUNT)

    def enter_user_details(
        self,
        first_name,
        last_name,
        email,
        password,
        confirm_password,
        telephone_number,
    ):
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.EMAIL, email)
        self.fill(self.TELEPHONE, telephone_number)
        self.fill(self.PASSWORD, password)
        self.fill(self.PASSWORD_CONFIRM, confirm_password)
        self.click(self.NEWSLETTER)
        self.click(self.PRIVACY_POLICY)
        self.click(self.SUBMIT_BUTTON)

    def register_user_Without_Data(self):
        self.click(self.SUBMIT_BUTTON)

    def verify_register_success_text(self):
        return self.get_text(self.Account_Success_Text)

    def Duplicate_Email_Warning_Retrieval(self):
        return self.get_text(self.Duplicate_Email_Warning)

    def No_Privacy_Policy_Warning(self):
        return self.get_text(self.Privacy_Policy_Warning)

    def No_First_Name_Warning(self):
        return self.get_text(self.First_Name_Warning)

    def No_Last_Name_Warning(self):
        return self.get_text(self.Last_Name_Warning)

    def No_Email_Warning(self):
        return self.get_text(self.EMail_Warning)

    def No_Password_Warning(self):
        return self.get_text(self.Password_Warning)

    def No_Telephone_Warning(self):
        return self.get_text(self.Telephone_Warning)

    def Open_Register_Page_In_Register_Page(self):
        self.click(self.Register_Option_In_Register_Page)

    def Verify_Register_Page_From_Personal_Details_Message(self):
        return self.get_text(self.Personal_Details_Confirm_Text)

    def Verify_Register_Without_Selecting_Private_Policy(
        self,
        first_name,
        last_name,
        email,
        password,
        confirm_password,
        telephone_number,
    ):
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.EMAIL, email)
        self.fill(self.TELEPHONE, telephone_number)
        self.fill(self.PASSWORD, password)
        self.fill(self.PASSWORD_CONFIRM, confirm_password)
        self.click(self.NEWSLETTER)
        self.click(self.SUBMIT_BUTTON)

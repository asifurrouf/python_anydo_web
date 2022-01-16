from pages.base_page import BasePage
from utils.locators import LoginPageLocator

class LoginPage(BasePage):
    def __init__(self,driver):
        super.__init__(driver)
        self.locator = LoginPageLocator

    def login_with_email_and_password(self, email, password):
        button = self.driver.find_element(*self.locator.LOGIN_WITH_EMAIL_BUTTON)
        button.click()
        email_txtbox = self.driver.find_element(*self.locator.EMAIL_TEXTBOX)
        email_submit_btn = self.driver.find_element(*self.locator.EMAIL_SUBMIT_BTN)
        email_submit_btn.click()
        self.driver.implicitly_wait(10)
        password_txtbox = self.driver.find_element(*self.locator.PASSWORD_TEXTBOX)
        email_txtbox.send_keys(email)
        password_txtbox.send_keys(password)
        login_button = self.driver.find_element(*self.locator.LOGIN_BTN)
        login_button.click()
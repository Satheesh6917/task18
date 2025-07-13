from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.XPATH, "//input[@placeholder='Enter your mail']")
        self.password_input = (By.XPATH, "//input[@placeholder='Enter your password ']")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        print(f"Attempting login with: {username}")
        self.driver.find_element(*self.email_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        time.sleep(3)

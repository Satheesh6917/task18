from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import time

@given("I launch the browser")
def step_launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://v2.zenclass.in/login")
    context.login_page = LoginPage(context.driver)

@when("I enter valid username and password")
def step_valid_login(context):
    context.login_page.login("satheeshkanna441@gmail.com", "Bakunamatata@123") 

@when("I enter invalid username and password")
def step_invalid_login(context):
    context.login_page.login("wronguser@gmail.com", "wrongpass")

@then("I should be redirected to the dashboard")
def step_dashboard_check(context):
    time.sleep(3)
    assert "dashboard" in context.driver.current_url.lower()

@then("I should see a login error message")
def step_error_check(context):
    time.sleep(2)
    error_elements = context.driver.find_elements(By.XPATH, "//div[contains(text(),'Invalid Credentials')]")
    assert len(error_elements) > 0, "Login error message not displayed"

@then("Username, Password fields and Submit button should be visible")
def step_check_elements(context):
    assert context.driver.find_element(By.XPATH, "//input[@placeholder='Enter your mail']").is_displayed()
    assert context.driver.find_element(By.XPATH, "//input[@placeholder='Enter your password ']").is_displayed()
    assert context.driver.find_element(By.XPATH, "//button[@type='submit']").is_displayed()

@given("I am logged into the Zen portal")
def step_logged_in(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://v2.zenclass.in/login")
    context.login_page = LoginPage(context.driver)
    context.login_page.login("satheeshkanna441@gmail.com", "Bakunamatata@123") 
    time.sleep(3)

@when("I click logout")
def step_logout(context):
    time.sleep(2)
    try:
        # Logout might be in a dropdown or side menu
        logout_button = context.driver.find_element(By.XPATH, "//button[contains(text(),'Logout')]")
        logout_button.click()
    except Exception as e:
        print("Logout failed:", e)
        raise

@then("I should be redirected to the login page")
def step_logged_out(context):
    time.sleep(2)
    assert "login" in context.driver.current_url.lower()

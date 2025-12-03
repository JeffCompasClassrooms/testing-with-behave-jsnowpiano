from behave_webdriver.steps import *
from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('I open the url "{url}" and wait')
def open_url_with_wait(context, url):
    context.behave_driver.get(url)
    time.sleep(2)

@when('I wait and set "{text}" to the inputfield "{selector}"')
def set_input_with_explicit_wait(context, text, selector):
    wait = WebDriverWait(context.behave_driver, 15)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    time.sleep(1)
    element.clear()
    element.send_keys(text)

@then('I wait and expect that element "{selector}" is visible')
def check_element_visible_with_explicit_wait(context, selector):
    wait = WebDriverWait(context.behave_driver, 15)
    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    assert element.is_displayed(), f"Element {selector} is not visible"

@then('I wait and expect that element "{selector}" is empty')
def check_element_empty_with_explicit_wait(context, selector):
    wait = WebDriverWait(context.behave_driver, 15)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    value = element.get_attribute('value') or element.text
    assert value == '', f"Element {selector} is not empty, contains: {value}"
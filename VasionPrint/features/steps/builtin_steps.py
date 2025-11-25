from behave_webdriver.steps import *
from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

@when('I right click on the element "{selector}"')
def right_click_element(context, selector):
    element = context.behave_driver.find_element(By.CSS_SELECTOR, selector)
    actions = ActionChains(context.behave_driver)
    actions.context_click(element).perform()

@when('I right click on the link "{link_text}"')
def right_click_link(context, link_text):
    element = context.behave_driver.find_element(By.LINK_TEXT, link_text)
    actions = ActionChains(context.behave_driver)
    actions.context_click(element).perform()

@when('I click on the tab "{tab_text}"')
def click_on_tab(context, tab_text):
    element = context.behave_driver.find_element(By.XPATH, f"//span[contains(@class, 'tabbutton') and contains(text(), '{tab_text}')]")
    element.click()

@then('I expect that a new tab has opened')
def check_new_tab_opened(context):
    assert len(context.behave_driver.window_handles) > 1, "No new tab was opened"

@given('I close the last opened tab')
def close_last_tab(context):
    if len(context.behave_driver.window_handles) > 1:
        context.behave_driver.switch_to.window(context.behave_driver.window_handles[-1])
        context.behave_driver.close()
        context.behave_driver.switch_to.window(context.behave_driver.window_handles[0])
from behave_webdriver.steps import *
from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

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

@given('I login to the admin portal')
def login_to_portal(context):
    context.behave_driver.get("https://jordansnow.printercloudnow.com/admin/")
    time.sleep(2)
    context.behave_driver.find_element(By.CSS_SELECTOR, "#login-username-field").send_keys("VasionTest")
    context.behave_driver.find_element(By.CSS_SELECTOR, "#login-password-field").send_keys("VasionTest")
    context.behave_driver.find_element(By.CSS_SELECTOR, "#sign-in-button").click()
    time.sleep(2)

@when('I add a printer named "{printer_name}" with IP "{ip_address}"')
def add_printer(context, printer_name, ip_address):
    time.sleep(1)
    context.behave_driver.find_element(By.LINK_TEXT, "New").click()
    time.sleep(1)
    context.behave_driver.find_element(By.CSS_SELECTOR, "#addip_link").click()
    time.sleep(1)
    context.behave_driver.find_element(By.CSS_SELECTOR, "#PrinterName").send_keys(printer_name)
    context.behave_driver.find_element(By.CSS_SELECTOR, "#IPAddress").send_keys(ip_address)
    context.behave_driver.find_element(By.CSS_SELECTOR, "#add_ip_close").click()
    time.sleep(1)

@when('I delete the printer "{printer_name}"')
def delete_printer(context, printer_name):
    time.sleep(1)
    element = context.behave_driver.find_element(By.LINK_TEXT, printer_name)
    actions = ActionChains(context.behave_driver)
    actions.context_click(element).perform()
    time.sleep(1)
    context.behave_driver.find_element(By.LINK_TEXT, "Delete").click()
    time.sleep(1)
    context.behave_driver.find_element(By.CSS_SELECTOR, "#delete_confirm_text").send_keys("DELETE")
    context.behave_driver.find_element(By.CSS_SELECTOR, "#delete_confirm_btn_ok").click()
    time.sleep(1)

@when('I rename the printer "{old_name}" to "{new_name}"')
def rename_printer(context, old_name, new_name):
    time.sleep(1)
    context.behave_driver.find_element(By.LINK_TEXT, old_name).click()
    time.sleep(1)
    title_field = context.behave_driver.find_element(By.CSS_SELECTOR, "#str_title")
    title_field.clear()
    title_field.send_keys(new_name)
    context.behave_driver.find_element(By.LINK_TEXT, "Save").click()
    time.sleep(1)
    # Navigate back to printer list
    context.behave_driver.find_element(By.LINK_TEXT, "Printers").click()
    time.sleep(1)

@when('I open printer "{printer_name}"')
def open_printer(context, printer_name):
    time.sleep(1)
    context.behave_driver.find_element(By.LINK_TEXT, printer_name).click()
    time.sleep(1)

@when('I set the printer name to "{new_name}"')
def set_printer_name(context, new_name):
    title_field = context.behave_driver.find_element(By.CSS_SELECTOR, "#str_title")
    title_field.clear()
    title_field.send_keys(new_name)
    context.behave_driver.find_element(By.LINK_TEXT, "Save").click()
    time.sleep(1)

@when('I change printer "{printer_name}" IP to "{new_ip}"')
def change_printer_ip(context, printer_name, new_ip):
    time.sleep(1)
    context.behave_driver.find_element(By.LINK_TEXT, printer_name).click()
    time.sleep(1)
    element = context.behave_driver.find_element(By.XPATH, f"//span[contains(@class, 'tabbutton') and contains(text(), 'Port')]")
    element.click()
    time.sleep(1)
    host_field = context.behave_driver.find_element(By.CSS_SELECTOR, "#str_host_address")
    host_field.clear()
    host_field.send_keys(new_ip)
    context.behave_driver.find_element(By.LINK_TEXT, "Save").click()
    time.sleep(1)
    # Navigate back to printer list
    context.behave_driver.find_element(By.LINK_TEXT, "Printers").click()
    time.sleep(1)

@when('I open printer "{printer_name}" Port settings')
def open_printer_port_settings(context, printer_name):
    time.sleep(1)
    context.behave_driver.find_element(By.LINK_TEXT, printer_name).click()
    time.sleep(1)
    element = context.behave_driver.find_element(By.XPATH, f"//span[contains(@class, 'tabbutton') and contains(text(), 'Port')]")
    element.click()
    time.sleep(1)

@when('I set the printer IP to "{new_ip}"')
def set_printer_ip(context, new_ip):
    host_field = context.behave_driver.find_element(By.CSS_SELECTOR, "#str_host_address")
    host_field.clear()
    host_field.send_keys(new_ip)
    context.behave_driver.find_element(By.LINK_TEXT, "Save").click()
    time.sleep(1)

@when('I open the help menu and click "{link_text}"')
def open_help_menu(context, link_text):
    context.behave_driver.find_element(By.CSS_SELECTOR, "#help-menu").click()
    context.behave_driver.find_element(By.LINK_TEXT, link_text).click()
    time.sleep(2)

@when('I navigate to "{setting_name}" settings')
def navigate_to_settings(context, setting_name):
    time.sleep(2)
    # Try to click return button if it exists and is visible
    try:
        return_button = context.behave_driver.find_element(By.CSS_SELECTOR, "#gear-return-button")
        if return_button.is_displayed():
            return_button.click()
            time.sleep(2)
    except:
        pass  # Button not found or not visible, continue
    
    context.behave_driver.find_element(By.CSS_SELECTOR, "#gear-menu").click()
    time.sleep(1)
    context.behave_driver.find_element(By.LINK_TEXT, "Settings").click()
    time.sleep(1)
    context.behave_driver.find_element(By.LINK_TEXT, setting_name).click()
    time.sleep(1)

@when('I access my account information')
def access_account(context):
    time.sleep(1)
    context.behave_driver.find_element(By.CSS_SELECTOR, "#user-menu").click()
    time.sleep(1)
    context.behave_driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(1)

@when('I logout')
def logout(context):
    time.sleep(1)
    context.behave_driver.find_element(By.CSS_SELECTOR, "#user-menu").click()
    time.sleep(1)
    context.behave_driver.find_element(By.LINK_TEXT, "Sign Out").click()
    time.sleep(3)

@then('the printer "{printer_name}" should be visible')
def verify_printer_visible(context, printer_name):
    body_text = context.behave_driver.find_element(By.TAG_NAME, "body").text
    assert printer_name in body_text, f"Printer {printer_name} not found"

@then('the printer "{printer_name}" should not be visible')
def verify_printer_not_visible(context, printer_name):
    body_text = context.behave_driver.find_element(By.TAG_NAME, "body").text
    assert printer_name not in body_text, f"Printer {printer_name} still visible"

@then('the printer name should be "{printer_name}"')
def verify_printer_name(context, printer_name):
    # Check the printer name field value on the current page (should already be on printer edit page)
    title_field = context.behave_driver.find_element(By.CSS_SELECTOR, "#str_title")
    assert printer_name in title_field.get_attribute("value"), f"Printer name is not {printer_name}"

@then('the printer IP should be "{ip_address}"')
def verify_printer_ip(context, ip_address):
    # Check the IP field value on the current page (should already be on Port tab)
    host_field = context.behave_driver.find_element(By.CSS_SELECTOR, "#str_host_address")
    assert ip_address in host_field.get_attribute("value"), f"IP is not {ip_address}"

@then('I should see "{text}" on the page')
def verify_text_on_page(context, text):
    body_text = context.behave_driver.find_element(By.TAG_NAME, "body").text
    assert text in body_text, f"Text '{text}' not found on page"
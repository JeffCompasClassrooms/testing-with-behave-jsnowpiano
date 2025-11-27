import behave_webdriver
from behave_webdriver.steps import *
import chromedriver_autoinstaller

def before_all(context):
    chromedriver_autoinstaller.install()  # Automatically installs ChromeDriver
    context.behave_driver = behave_webdriver.Chrome()  # Use `context.behave_driver`

def after_all(context):
    context.behave_driver.quit()

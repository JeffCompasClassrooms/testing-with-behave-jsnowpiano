import behave_webdriver
from behave_webdriver.steps import *
import chromedriver_autoinstaller

def before_all(context):
    chromedriver_autoinstaller.install()
    context.behave_driver = behave_webdriver.Chrome()

def after_all(context):
    if hasattr(context, 'behave_driver'):
        context.behave_driver.quit()
import behave_webdriver
from behave_webdriver.steps import *
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

def before_all(context):
    chromedriver_autoinstaller.install()
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    
    context.behave_driver = behave_webdriver.Chrome(options=chrome_options)
    context.wait = WebDriverWait(context.behave_driver, 10)

def after_all(context):
    if hasattr(context, 'behave_driver'):
        context.behave_driver.quit()
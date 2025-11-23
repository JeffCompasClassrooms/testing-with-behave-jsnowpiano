from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get('https://kb.printerlogic.com/s/knowledge-base')
time.sleep(3)

print('Looking for "Administrator Console" link...\n')

# Check if the link exists
try:
    link = driver.find_element(By.LINK_TEXT, 'Administrator Console')
    print('✓ Found link by LINK_TEXT')
    print(f'  Href: {link.get_attribute("href")}')
    print(f'  Class: {link.get_attribute("class")}')
except:
    print('✗ Not found by LINK_TEXT')

# Check by partial link text
try:
    link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Administrator')
    print('✓ Found link by PARTIAL_LINK_TEXT')
    print(f'  Text: {link.text}')
except:
    print('✗ Not found by PARTIAL_LINK_TEXT')

# Check by class
try:
    link = driver.find_element(By.CSS_SELECTOR, 'a.topicHeaderLink')
    print('✓ Found link by class "topicHeaderLink"')
    print(f'  Text: {link.text}')
    print(f'  Title: {link.get_attribute("title")}')
except:
    print('✗ Not found by class topicHeaderLink')

# List all links with "console" in text
all_links = driver.find_elements(By.TAG_NAME, 'a')
console_links = [l for l in all_links if 'console' in l.text.lower() or 'console' in l.get_attribute('title').lower() if l.get_attribute('title')]
print(f'\nFound {len(console_links)} links with "console" in text or title:')
for link in console_links[:5]:
    print(f'  - Text: "{link.text[:50]}" | Title: "{link.get_attribute("title")}"')

driver.quit()

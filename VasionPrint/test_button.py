from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

print('='*60)
print('STEP 1: Opening URL')
print('='*60)
driver.get('https://jordansnow.printercloudnow.com/admin/')
time.sleep(2)
print('✓ URL opened')

print('\n' + '='*60)
print('STEP 2: Filling in login credentials')
print('='*60)
try:
    username = driver.find_element(By.CSS_SELECTOR, '#login-username-field')
    print(f'✓ Found username field')
    username.send_keys('VasionTest')
    print('✓ Entered username')
    
    password = driver.find_element(By.CSS_SELECTOR, '#login-password-field')
    print(f'✓ Found password field')
    password.send_keys('VasionTest')
    print('✓ Entered password')
    
    signin = driver.find_element(By.CSS_SELECTOR, '#sign-in-button')
    print(f'✓ Found sign-in button')
    signin.click()
    print('✓ Clicked sign-in button')
except Exception as e:
    print(f'✗ Login failed: {e}')
    driver.quit()
    exit()

print('\n' + '='*60)
print('STEP 3: Waiting 7 seconds for dashboard to load')
print('='*60)
time.sleep(7)
print('✓ Wait complete')

print('\n' + '='*60)
print('STEP 4: Looking for #newfolder button')
print('='*60)
try:
    newfolder = driver.find_element(By.CSS_SELECTOR, '#newfolder')
    print(f'✓ Found #newfolder')
    print(f'  Text: "{newfolder.text}"')
    print(f'  Visible: {newfolder.is_displayed()}')
    print(f'  Enabled: {newfolder.is_enabled()}')
    print(f'  Tag: {newfolder.tag_name}')
    
    print('\nClicking #newfolder...')
    newfolder.click()
    print('✓ Clicked #newfolder')
except Exception as e:
    print(f'✗ Failed to find/click #newfolder: {e}')
    driver.quit()
    exit()

print('\n' + '='*60)
print('STEP 5: Waiting 3 seconds for dropdown')
print('='*60)
time.sleep(3)
print('✓ Wait complete')

print('\n' + '='*60)
print('STEP 6: Looking for #addip_link')
print('='*60)
try:
    addip = driver.find_element(By.CSS_SELECTOR, '#addip_link')
    print(f'✓ Found #addip_link')
    print(f'  Text: "{addip.text}"')
    print(f'  Visible: {addip.is_displayed()}')
    
    print('\nClicking #addip_link...')
    addip.click()
    print('✓ Clicked #addip_link')
except Exception as e:
    print(f'✗ Failed to find/click #addip_link: {e}')
    driver.quit()
    exit()

print('\n' + '='*60)
print('STEP 7: Waiting 3 seconds for form to load')
print('='*60)
time.sleep(3)
print('✓ Wait complete')

print('\n' + '='*60)
print('STEP 8: Filling printer details form')
print('='*60)
try:
    printer_name = driver.find_element(By.CSS_SELECTOR, '#PrinterName')
    print(f'✓ Found #PrinterName field')
    printer_name.send_keys('TempTestPrinter')
    print('✓ Entered printer name')
    
    ip_address = driver.find_element(By.CSS_SELECTOR, '#IPAddress')
    print(f'✓ Found #IPAddress field')
    ip_address.send_keys('0.0.0.0')
    print('✓ Entered IP address')
except Exception as e:
    print(f'✗ Failed to fill form: {e}')
    driver.quit()
    exit()

print('\n' + '='*60)
print('STEP 9: Clicking close button')
print('='*60)
try:
    close_btn = driver.find_element(By.CSS_SELECTOR, '#add_ip_close')
    print(f'✓ Found #add_ip_close')
    close_btn.click()
    print('✓ Clicked close button')
except Exception as e:
    print(f'✗ Failed to click close: {e}')
    driver.quit()
    exit()

print('\n' + '='*60)
print('STEP 10: Waiting 3 seconds and checking for printer')
print('='*60)
time.sleep(3)
body_text = driver.find_element(By.TAG_NAME, 'body').text
if 'TempTestPrinter' in body_text:
    print('✓ SUCCESS! Found "TempTestPrinter" in page body')
else:
    print('✗ FAILED! "TempTestPrinter" not found in page body')
    print(f'\nBody text sample (first 500 chars):')
    print(body_text[:500])

print('\n' + '='*60)
print('TEST COMPLETE')
print('='*60)

time.sleep(3)
driver.quit()

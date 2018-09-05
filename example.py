# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import os
import datetime
# chrome_options = Options()
# chrome_options.add_argument('--log-level=0')
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")
# chrome_driver = "/usr/local/bin/chromedriver"


# # Google Chrome
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
print(datetime.datetime.now())
chrome_options = Options()
chrome_options.add_argument("--headless")

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptSslCerts'] = True
capabilities['acceptInsecureCerts'] = True

driver = webdriver.Chrome(chrome_options = chrome_options,executable_path='/usr/local/bin/chromedriver',desired_capabilities=capabilities)


# ------------------------------
# The actual test scenario: Test the codepad.org code execution service.

# Go to codepad.org
driver.get('https://esaj.tjsp.jus.br/cpopg/open.do')

# Enter some text!
text_area = driver.find_element_by_id('numeroDigitoAnoUnificado')
text_area.send_keys("0006656-58.2018")

# Enter some text!
text_area2 = driver.find_element_by_id('foroNumeroUnificado')
text_area2.send_keys("0481")

# Submit the form!
submit_button = driver.find_element_by_name('pbEnviar')
submit_button.click()

# Make this an actual test. Isn't Python beautiful?
bodyText = driver.find_element_by_tag_name('body').text
assert("Dados do processo" in bodyText)

text = driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr/td/div[1]/table[2]/tbody/tr[8]/td[2]/span").text
print(text)


# Close the browser!
print(datetime.datetime.now())
driver.quit()
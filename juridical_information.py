from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import names
import pyperclip
from login import hc_command
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
site = config['ENVIROMENT']['site']

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(site)

test = hc_command()
time.sleep(2)
test.open_user_agreement(driver)
test.open_privacy_policy(driver)
test.open_signin_form(driver)
time.sleep(1)

window_before = driver.window_handles[0]

driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
time.sleep(2)
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.find_element_by_xpath("//a[contains(text(),'Политика конфиденциальности')]").click()
time.sleep(1)
test.check_privacy_policy(driver)
driver.switch_to.window(window_before)


driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
time.sleep(2)
window_after = driver.window_handles[2]
driver.switch_to.window(window_after)
driver.find_element_by_xpath("//a[contains(text(),'Пользовательское соглашение')]").click()
time.sleep(1)
test.check_user_agreement(driver)
driver.switch_to.window(window_before)

driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
time.sleep(2)
window_after = driver.window_handles[3]
driver.switch_to.window(window_after)
driver.find_element_by_xpath("//a[contains(text(),'Правила проведения акции')]").click()
time.sleep(1)
driver.find_element_by_xpath("//li[contains(text(),'Организатор Акции ООО «Е09»')]")
driver.switch_to.window(window_before)

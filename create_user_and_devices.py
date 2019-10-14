from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import names
import pyperclip
from login import hc_command
import configparser

test = hc_command()

config = configparser.ConfigParser()
config.read('config.ini')
email = config['USER INFO']['email']
password = "23072307"

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(test.site())
time.sleep(1)

test.signin_parametr(driver, email, password)
test.setting(driver)
test.setting_devices(driver)
test.add_user(driver)
test.add_devices(driver)

# Сюда бы чеки еще написать на проверку, ну хуй с ними потом напишем

driver.close()
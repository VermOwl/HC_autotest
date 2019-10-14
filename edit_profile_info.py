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
temp = config['USER INFO']['email']
password = "23072307"

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(test.site())

#Изменение основной информации
test.signin_parametr(driver, temp, password)
test.setting(driver)
test.add_profile_info(driver)

#Проверка информации о пользователе
driver.close()
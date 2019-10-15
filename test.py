from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import names
import pyperclip
from login import hc_command
import configparser
import logging
import getpass

test = hc_command()

username = getpass.getuser()
print(username)

config = configparser.ConfigParser()
config.read('config.ini')
temp = config['USER INFO']['email']
password = "23072307"

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(test.site())

test.signin(driver)
test.support_message(driver)

driver.close()
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
config.read('environment.ini')
site = config['ENVIRONMENT']['site']

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(site)

test = hc_command()

test.feedback_form(driver)

driver.close()
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

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://front.stage.helpcubes.com/legal-docs")

test = hc_command()

time.sleep(1)

driver.find_element_by_xpath("//a[contains(text(),'Политика конфиденциальности')]").click()

driver.close()
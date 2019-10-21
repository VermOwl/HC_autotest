from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random
import names
import pyperclip
import configparser
import logging
import getpass
import re
from colorama import Fore, Style

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }    
driver = webdriver.Chrome(desired_capabilities=d, chrome_options=chrome_options)

driver.get('http://foo.com')
# print messages
if driver.name == 'chrome':
    st = driver.name
    st_2 = "sdf"
    print ("lfhjdf t,fnm")
    for entry in driver.get_log('browser'):
        print (entry)
else:
    print ("mozilla")

driver.quit()

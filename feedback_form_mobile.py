from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import names
import pyperclip
from login_mobile import hc_command_mobile
import configparser
from browsers import browsers

def feedback_form_mobile(driver):
    
    test = hc_command_mobile()
    driver.get(test.site())
    test.feedback_form(driver)
    driver.quit()

#browser = browsers()
#driver = browser.chrome_mobile()
#feedback_form_mobile(driver)
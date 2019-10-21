from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import names
import pyperclip
from login import hc_command
import configparser
from browsers import browsers

def feedback_form(driver):
    
    test = hc_command()
    driver.get(test.site())
    test.feedback_form(driver)

    browser = browsers()
    browser.quit_browser(driver)
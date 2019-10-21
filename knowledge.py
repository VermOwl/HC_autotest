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
from login_mobile import hc_command_mobile

def knowledge(driver):
    
    test = hc_command()
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    temp = config['USER INFO']['email']
    password = "23072307"

    driver.get(test.site())
    test.signin_parametr(driver, temp, password)
    #test.knowledge_search_field(driver)
    test.tag_filter(driver)
    
    
    browser = browsers()
    browser.quit_browser(driver)


browser = browsers()
driver = browser.chrome()
knowledge(driver)
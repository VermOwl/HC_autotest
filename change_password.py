from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import names
import pyperclip
from login import hc_command
import configparser
from colorama import Fore, Style
from browsers import browsers

def change_password (driver):
    test = hc_command()

    config = configparser.ConfigParser()
    config.read('config.ini')
    email = config['USER INFO']['email']
    password = "23072307"
    if "http://" in test.site():
        driver.get(test.site())
    else: 
        print ("Info: сайти использует https - падаем") 
        assert False

    driver.implicitly_wait(10)

    test.signin_parametr(driver, email, password)
    test.setting(driver)
    test.change_password(driver)

#browser = browsers()
#driver = browser.chrome()
#change_password(driver)


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


def edit_user_and_device(driver):
    test = hc_command()

    config = configparser.ConfigParser()
    config.read('config.ini')
    email = config['USER INFO']['email']
    password = "23072307"

    driver.get(test.site())
    driver.implicitly_wait(10)
    driver.execute_script("$nuxt.$loading = { };")


    test.signin_parametr(driver, email, password)
    test.setting(driver)
    test.setting_devices(driver)
    test.edit_user(driver)
    test.user_delete(driver)
    test.device_edit(driver)
    test.device_delete(driver)


    browser = browsers()
    browser.close_browser(driver)

#browser = browsers()
#driver = browser.chrome()
#edit_user_and_device(driver)

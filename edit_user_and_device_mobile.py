from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import names
import pyperclip
from login_mobile import hc_command_mobile
import configparser
from colorama import Fore, Style
from browsers import browsers


def edit_user_and_device_mobile(driver):
    test = hc_command_mobile()

    config = configparser.ConfigParser()
    config.read('config.ini')
    email = config['USER INFO']['email']
    password = "23072307"

    driver.get(test.site())
    driver.implicitly_wait(10)

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
#driver = browser.chrome_mobile()
#edit_user_and_device(driver)

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


def create_user_and_devices_mobile(driver):
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
    test.add_user(driver)
    test.add_devices(driver)

    browser = browsers()
    browser.quit_browser(driver)


#browser = browsers()
#driver = browser.chrome_mobile()
#create_user_and_devices_mobile(driver)
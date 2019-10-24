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

def add_user_with_send_support(driverTemp):
    test = hc_command()

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://temp-mail.org/ru/")

    driverTemp.get(test.site())
    driverTemp.implicitly_wait(10)
    driver.implicitly_wait(10)

    test.getmail(driver)
    test.registration(driverTemp)
    test.confirm_mail(driver)

    config = configparser.ConfigParser()
    config ['USER INFO']= {'email': pyperclip.paste()}
    with open('config.ini', 'w+') as configfile:
        config.write(configfile)

    test.signin(driverTemp)
    test.tariff_add(driverTemp)
    test.setting(driverTemp)
    test.setting_devices(driverTemp)
    test.add_devices(driverTemp)
    test.support_message(driverTemp)

    driver.close()

    browser = browsers()
    browser.close_browser(driverTemp)

#browser = browsers()
#driver = browser.chrome()
#add_user_with_send_support(driver)
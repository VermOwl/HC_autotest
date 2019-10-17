from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import names
import pyperclip
from login import hc_command
import configparser

def card_information(driver):
    config = configparser.ConfigParser()
    config.read('config.ini')
    mail = config['USER INFO']['email']
    password = "23072307"

    test = hc_command()

    driver.get(test.site())

    test.signin_parametr(driver, mail, password)
    test.setting(driver)
    test.setting_credit_card(driver)
    test.cahnge_renew(driver)
    test.payment_method_change_delete_add(driver)
    driver.quit()
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

def edit_profile_info_mobile(driver):
    test = hc_command_mobile()

    config = configparser.ConfigParser()
    config.read('config.ini')
    temp = config['USER INFO']['email']
    password = "23072307"

    driver.get(test.site())
    driver.implicitly_wait(10)
    
    #Изменение основной информации
    test.signin_parametr(driver, temp, password)
    test.setting(driver)
    test.add_profile_info(driver)

    #Проверка информации о пользователе
    browser = browsers()
    browser.quit_browser(driver)

#browser = browsers()
#driver = browser.chrome_mobile()
#edit_profile_info_mobile(driver)
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
from selenium.webdriver.common.action_chains import ActionChains


def main_page_check_unatorize_mobile(driver):
    test = hc_command_mobile()
    
    driver.get(test.site())
    driver.implicitly_wait(10)
    #test.main_page_check(driver)
    #test.footer_unauthorized(driver)
    #test.main_sevices(driver)
    #test.main_how_its_work(driver)
    test.main_tarifs(driver)


    browser = browsers()
    browser.quit_browser(driver)

#browser = browsers()
#driver = browser.mozilla_mobile()
#main_page_check_unatorize(driver)

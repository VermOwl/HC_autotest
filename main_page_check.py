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

def main_page_check_unatorize(driver):
    test = hc_command()
    
    driver.get(test.site())
    driver.implicitly_wait(10)
    driver.execute_script("$nuxt.$loading = { };")


    test.main_page_check(driver)
    test.footer_unauthorized(driver)
    test.main_sevices(driver)
    test.main_how_its_work(driver)
    test.main_tarifs(driver)


    browser = browsers()
    browser.quit_browser(driver)

#browser = browsers()
#driver = browser.chrome()
##print (Fore.CYAN + "edit_profile_info" + Style.RESET_ALL)
#main_page_check_unatorize(driver)

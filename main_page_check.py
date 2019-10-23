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

def edit_profile_info(driver):
    test = hc_command()
    
    driver.get(test.site())

    test.main_page_check(driver)


    browser = browsers()
    browser.quit_browser(driver)

browser = browsers()
driver = browser.mozilla()
#print (Fore.CYAN + "edit_profile_info" + Style.RESET_ALL)
edit_profile_info(driver)

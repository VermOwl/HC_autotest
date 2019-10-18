from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

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

desired_cap = {
 'browserName': 'iPhone',
 'device': 'iPhone 8 Plus',
 'realMobile': 'true',
 'os_version': '11',
 'name': 'Bstack-[Python] Sample Test'
}

driver = webdriver.Remote(
    command_executor='http://hpaysrv1:FrNZzzsdLptqjxkKtNEr@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)


def feedback_form_mobile(driver):
    
    test = hc_command_mobile()
    driver.get(test.site())
    test.feedback_form(driver)
    driver.quit()

feedback_form_mobile(driver)

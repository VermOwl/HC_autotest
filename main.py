from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import names
import pyperclip
from login import hc_command
import configparser
import logging
import getpass

from browsers import browsers

from add_user_with_send_support import add_user_with_send_support
from card_information import card_information
from create_user_and_devices import create_user_and_devices
from edit_profile_info import edit_profile_info
from feedback_form import feedback_form
from juridical_information import juridical_information

def chrome_test():
    browser = browsers()
    driver = browser.chrome()

    try:
        k = add_user_with_send_support()
        k.add_user_with_send_support(driver)
    except Exception as e:
        print (e)
    try: 
        edit_profile_info(driver)
    except Exception as e:
        print (e)
    try:
        create_user_and_devices(driver)
    except Exception as e:
        print (e)
    #card_information(driver)
    try:
        feedback_form(driver)
    except Exception as e:
        print (e)
    try:
        juridical_information(driver)
    except Exception as e:
        print (e)

def mozilla_test():
    browser = browsers()
    driver = browser.mozilla()

    try:
        add_user_with_send_support(driver)
    except Exception as e:
        print (e)
    try: 
        edit_profile_info(driver)
    except Exception as e:
        print (e)
    try:
        create_user_and_devices(driver)
    except Exception as e:
        print (e)
    #card_information(driver)
    try:
        feedback_form(driver)
    except Exception as e:
        print (e)
    try:
        juridical_information(driver)
    except Exception as e:
        print (e)

chrome_test()
mozilla_test()

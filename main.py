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
import colorama
from colorama import Fore, Style
import traceback

from browsers import browsers

from add_user_with_send_support import add_user_with_send_support
from card_information import card_information
from create_user_and_devices import create_user_and_devices
from edit_profile_info import edit_profile_info
from feedback_form import feedback_form
from juridical_information import juridical_information

from add_user_with_send_support_mobile import add_user_with_send_support_mobile
from edit_profile_info_mobile import edit_profile_info_mobile

def chrome_test():
    try:
        browser = browsers()
        driver = browser.chrome()
        add_user_with_send_support(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.chrome() 
        edit_profile_info(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        print (Style.RESET_ALL)
    
    try:
        browser = browsers()
        driver = browser.chrome()
        create_user_and_devices(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        print (Style.RESET_ALL)
    #card_information(driver)
    
    try:
        browser = browsers()
        driver = browser.chrome()
        feedback_form(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        print (Style.RESET_ALL)
    
    try:
        browser = browsers()
        driver = browser.chrome()
        test = juridical_information()
        test.juridical_information(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.chrome()
        test = juridical_information()
        test.juridical_information_part2_chrome(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        print (Style.RESET_ALL)

def mozilla_test():

    try:
        browser = browsers()
        driver = browser.mozilla()
        add_user_with_send_support(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        print (Style.RESET_ALL)
    
    try:
        browser = browsers()
        driver = browser.mozilla() 
        edit_profile_info(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        print (Style.RESET_ALL)
    
    try:
        browser = browsers()
        driver = browser.mozilla() 
        create_user_and_devices(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        print (Style.RESET_ALL)
    #card_information(driver)
    
    try:
        browser = browsers()
        driver = browser.mozilla() 
        feedback_form(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        print (Style.RESET_ALL)
    
    try:
        browser = browsers()
        driver = browser.mozilla() 
        test = juridical_information()
        test.juridical_information(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.mozilla() 
        test = juridical_information()
        test.juridical_information_part2_mozilla(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        print (Style.RESET_ALL)

def chrome_test_mobile ():

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        add_user_with_send_support_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        edit_profile_info_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        print (Style.RESET_ALL)


def test(case, driver):
    print("nice")



chrome_test()
mozilla_test()
chrome_test_mobile()

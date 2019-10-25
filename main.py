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
import inspect
import threading

from browsers import browsers

from add_user_with_send_support import add_user_with_send_support
from card_information import card_information
from create_user_and_devices import create_user_and_devices
from edit_profile_info import edit_profile_info
from feedback_form import feedback_form
from juridical_information import juridical_information
from knowledge import knowledge
from main_page_check import main_page_check_unatorize
from main_page_check_mobile import main_page_check_unatorize_mobile

from add_user_with_send_support_mobile import add_user_with_send_support_mobile
from edit_profile_info_mobile import edit_profile_info_mobile
from create_user_and_devices_mobile import create_user_and_devices_mobile
from feedback_form_mobile import feedback_form_mobile
from juridical_information_mobile import juridical_information_mobile
from knowledge_mobile import knowledge_mobile

def chrome_test():
    try:
        browser = browsers()
        driver = browser.chrome()
        print (Fore.CYAN + "chrome test add_user_with_send_support" + Style.RESET_ALL)
        add_user_with_send_support(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.chrome() 
        print (Fore.CYAN + "chrome test edit profile info" + Style.RESET_ALL)
        edit_profile_info(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
    
    try:
        browser = browsers()
        driver = browser.chrome()
        print (Fore.CYAN + "chrome test create user and devices" + Style.RESET_ALL)
        create_user_and_devices(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
    #card_information(driver)
    
    try:
        browser = browsers()
        driver = browser.chrome()
        print (Fore.CYAN + "chrome test feedback form" + Style.RESET_ALL)
        feedback_form(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
    
    try:
        browser = browsers()
        driver = browser.chrome()
        test = juridical_information()
        print (Fore.CYAN + "chrome test juridical information" + Style.RESET_ALL)
        test.juridical_information(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.chrome()
        test = juridical_information()
        print (Fore.CYAN + "chrome test juridical information part 2" + Style.RESET_ALL)
        test.juridical_information_part2_chrome(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.chrome()
        print (Fore.CYAN + "chrome test knowledge" + Style.RESET_ALL)
        knowledge(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.chrome()
        print (Fore.CYAN + "chrome test site check element unautorization" + Style.RESET_ALL)
        main_page_check_unatorize(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

def mozilla_test():

    try:
        browser = browsers()
        driver = browser.mozilla()
        print (Fore.CYAN + "mozilla test add user with send support" + Style.RESET_ALL)
        add_user_with_send_support(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
    
    try:
        browser = browsers()
        driver = browser.mozilla() 
        print (Fore.CYAN + "mozilla test edit profile info" + Style.RESET_ALL)
        edit_profile_info(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
    
    try:
        browser = browsers()
        driver = browser.mozilla() 
        print (Fore.CYAN + "mozilla test create user and devices" + Style.RESET_ALL)
        create_user_and_devices(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
    #card_information(driver)
    
    try:
        browser = browsers()
        driver = browser.mozilla() 
        print (Fore.CYAN + "mozilla test feedback_form" + Style.RESET_ALL)
        feedback_form(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
    
    try:
        browser = browsers()
        driver = browser.mozilla() 
        test = juridical_information()
        print (Fore.CYAN + "mozilla test juridical information" + Style.RESET_ALL)
        test.juridical_information(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.mozilla() 
        test = juridical_information()
        print (Fore.CYAN + "mozilla test juridical information part 2" + Style.RESET_ALL)
        test.juridical_information_part2_mozilla(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.mozilla()
        print (Fore.CYAN + "mozilla test knowledge" + Style.RESET_ALL)
        knowledge(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.mozilla()
        print (Fore.CYAN + "mozilla test main_page_check_unatorize" + Style.RESET_ALL)
        main_page_check_unatorize(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
    
def chrome_test_mobile ():

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        print (Fore.CYAN + "chrome test mobile add user with send support" + Style.RESET_ALL)
        add_user_with_send_support_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        print (Fore.CYAN + "chrome test mobile edit profile info mobile" + Style.RESET_ALL)
        edit_profile_info_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        print (Fore.CYAN + "chrome test mobile create user and devices" + Style.RESET_ALL)
        create_user_and_devices_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        print (Fore.CYAN + "chrome test mobile feedback form" + Style.RESET_ALL)
        feedback_form_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        test = juridical_information_mobile()
        print (Fore.CYAN + "chrome test mobile juridical information" + Style.RESET_ALL)
        test.juridical_information_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        test = juridical_information_mobile()
        print (Fore.CYAN + "chrome test juridical information part 2" + Style.RESET_ALL)
        test.juridical_information_part2_chrome_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        print (Fore.CYAN + "chrome test mobile knowledge page" + Style.RESET_ALL)
        knowledge_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        print (Fore.CYAN + "chrome test mobile main_page_check_unatorize_mobile" + Style.RESET_ALL)
        main_page_check_unatorize_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

def mozilla_test_mobile ():

    try:
        browser = browsers()
        driver = browser.mozilla_mobile()
        print (Fore.CYAN + "mozilla test mobile add user with send support" + Style.RESET_ALL)
        add_user_with_send_support_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.mozilla_mobile()
        print (Fore.CYAN + "mozilla test mobile edit profile info mobile" + Style.RESET_ALL)
        edit_profile_info_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.mozilla_mobile()
        print (Fore.CYAN + "mozilla test mobile create user and devices" + Style.RESET_ALL)
        create_user_and_devices_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.mozilla_mobile()
        print (Fore.CYAN + "mozilla test mobile feedback form" + Style.RESET_ALL)
        feedback_form_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.mozilla_mobile()
        test = juridical_information_mobile()
        print (Fore.CYAN + "mozilla test mobile juridical information" + Style.RESET_ALL)
        test.juridical_information_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.mozilla_mobile()
        test = juridical_information_mobile()
        print (Fore.CYAN + "mozilla test juridical information part 2" + Style.RESET_ALL)
        test.juridical_information_part2_mozilla_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.mozilla_mobile()
        print (Fore.CYAN + "mozilla test mobile knowledge" + Style.RESET_ALL)
        knowledge_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

    try:
        browser = browsers()
        driver = browser.mozilla_mobile()
        print (Fore.CYAN + "mozilla test mobile main_page_check_unatorize_mobile" + Style.RESET_ALL)
        main_page_check_unatorize_mobile(driver)
    except Exception as e:
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)

def test(case, driver):
    print("nice")

chrome_test()
mozilla_test()
chrome_test_mobile()
mozilla_test_mobile()


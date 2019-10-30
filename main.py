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
import psutil
import time
import calendar

from browsers import browsers

from add_user_with_send_support import add_user_with_send_support
from card_information import card_information
from create_user_and_devices import create_user_and_devices
from edit_profile_info import edit_profile_info
from feedback_form import feedback_form
from juridical_information import juridical_information
from knowledge import knowledge
from main_page_check import main_page_check_unatorize
from edit_user_and_device import edit_user_and_device
from change_password import change_password

from add_user_with_send_support_mobile import add_user_with_send_support_mobile
from edit_profile_info_mobile import edit_profile_info_mobile
from create_user_and_devices_mobile import create_user_and_devices_mobile
from feedback_form_mobile import feedback_form_mobile
from juridical_information_mobile import juridical_information_mobile
from knowledge_mobile import knowledge_mobile
from main_page_check_mobile import main_page_check_unatorize_mobile
from edit_user_and_device_mobile import edit_user_and_device_mobile

def kill_chrome_driver(): # закрытие всех драйверов
    chromedriver = "chromedriver.exe"
    for proc in psutil.process_iter():
        if proc.name() == chromedriver:
            proc.kill()

def kill_mozilla_driver(): #
    chromedriver = "chromedriver.exe"
    for proc in psutil.process_iter():
        if proc.name() == chromedriver:
            proc.kill()

def make_screenshot(driver):
    '''
    Метод создания скриншотов
    Если тест падает вызывается этот метод который делает скриншот и помещает в рабочую_папку/screenshot/

    '''
    current_time = calendar.timegm(time.gmtime())
    print ("screenshot crush name = " + str(current_time))
    driver.save_screenshot("./Screenshots/" + str(current_time) + ".png")

def shell_test_chrome(method): 
    '''
    Это оболочка для тесоов. В качестве переменной сюда передается метод с самим кейсом
    Все завернуто в трайкетч. Eсли тест падает, запускается слудюущий метод
    Метод делает скрины при падении
    Метод пишет эксепшен
    '''

    try:
        browser = browsers()
        driver = browser.chrome()
        print (Fore.CYAN + "chrome test " + method.__name__ + "" + Style.RESET_ALL)
        method(driver) # вызов рабочего метода
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        #driver.quit()
        browser = browsers()
        browser.close_browser(driver)
    kill_chrome_driver()

def start_test_chrome_desktop (): # Метод передачи тестовых методов в рабочую оболочку
    shell_test_chrome(add_user_with_send_support)
    shell_test_chrome(edit_profile_info)
    shell_test_chrome(create_user_and_devices)
    shell_test_chrome(feedback_form)
    
    test = juridical_information()
    shell_test_chrome(test.juridical_information)
    shell_test_chrome(test.juridical_information_part2_chrome)

    shell_test_chrome(knowledge)
    shell_test_chrome(main_page_check_unatorize)
    shell_test_chrome(edit_user_and_device)
    shell_test_chrome(change_password)

start_test_chrome_desktop()



def mozilla_test():

    try:
        browser = browsers()
        driver = browser.mozilla()
        print (Fore.CYAN + "mozilla test add user with send support" + Style.RESET_ALL)
        add_user_with_send_support(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()
    
    try:
        browser = browsers()
        driver = browser.mozilla() 
        print (Fore.CYAN + "mozilla test edit profile info" + Style.RESET_ALL)
        edit_profile_info(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()
    
    try:
        browser = browsers()
        driver = browser.mozilla() 
        print (Fore.CYAN + "mozilla test create user and devices" + Style.RESET_ALL)
        create_user_and_devices(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()
    #card_information(driver)
    
    try:
        browser = browsers()
        driver = browser.mozilla() 
        print (Fore.CYAN + "mozilla test feedback_form" + Style.RESET_ALL)
        feedback_form(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()
    
    try:
        browser = browsers()
        driver = browser.mozilla() 
        test = juridical_information()
        print (Fore.CYAN + "mozilla test juridical information" + Style.RESET_ALL)
        test.juridical_information(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.mozilla() 
        test = juridical_information()
        print (Fore.CYAN + "mozilla test juridical information part 2" + Style.RESET_ALL)
        test.juridical_information_part2_mozilla(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.mozilla()
        print (Fore.CYAN + "mozilla test knowledge" + Style.RESET_ALL)
        knowledge(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.mozilla()
        print (Fore.CYAN + "mozilla test main_page_check_unatorize" + Style.RESET_ALL)
        main_page_check_unatorize(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.mozilla()
        print (Fore.CYAN + "mozilla test edit_user_and_device" + Style.RESET_ALL)
        edit_user_and_device(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.mozilla()
        print (Fore.CYAN + "mozilla test change_password" + Style.RESET_ALL)
        change_password(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()       
    
def chrome_test_mobile ():

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        print (Fore.CYAN + "chrome test mobile add user with send support" + Style.RESET_ALL)
        add_user_with_send_support_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        print (Fore.CYAN + "chrome test mobile edit profile info mobile" + Style.RESET_ALL)
        edit_profile_info_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        print (Fore.CYAN + "chrome test mobile create user and devices" + Style.RESET_ALL)
        create_user_and_devices_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        print (Fore.CYAN + "chrome test mobile feedback form" + Style.RESET_ALL)
        feedback_form_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        test = juridical_information_mobile()
        print (Fore.CYAN + "chrome test mobile juridical information" + Style.RESET_ALL)
        test.juridical_information_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        test = juridical_information_mobile()
        print (Fore.CYAN + "chrome test juridical information part 2" + Style.RESET_ALL)
        test.juridical_information_part2_chrome_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        print (Fore.CYAN + "chrome test mobile knowledge page" + Style.RESET_ALL)
        knowledge_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        print (Fore.CYAN + "chrome test mobile main_page_check_unatorize_mobile" + Style.RESET_ALL)
        main_page_check_unatorize_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.chrome_mobile()
        print (Fore.CYAN + "chrome test mobile edit_user_and_device_mobile" + Style.RESET_ALL)
        edit_user_and_device_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()


def mozilla_test_mobile ():

    try:
        browser = browsers()
        driver = browser.mozilla_mobile()
        print (Fore.CYAN + "mozilla test mobile add user with send support" + Style.RESET_ALL)
        add_user_with_send_support_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.mozilla_mobile()
        print (Fore.CYAN + "mozilla test mobile edit profile info mobile" + Style.RESET_ALL)
        edit_profile_info_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.mozilla_mobile()
        print (Fore.CYAN + "mozilla test mobile create user and devices" + Style.RESET_ALL)
        create_user_and_devices_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.mozilla_mobile()
        print (Fore.CYAN + "mozilla test mobile feedback form" + Style.RESET_ALL)
        feedback_form_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.mozilla_mobile()
        test = juridical_information_mobile()
        print (Fore.CYAN + "mozilla test mobile juridical information" + Style.RESET_ALL)
        test.juridical_information_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.mozilla_mobile()
        test = juridical_information_mobile()
        print (Fore.CYAN + "mozilla test juridical information part 2" + Style.RESET_ALL)
        test.juridical_information_part2_mozilla_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.mozilla_mobile()
        print (Fore.CYAN + "mozilla test mobile knowledge" + Style.RESET_ALL)
        knowledge_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

    try:
        browser = browsers()
        driver = browser.mozilla_mobile()
        print (Fore.CYAN + "mozilla test mobile edit_user_and_device_mobile" + Style.RESET_ALL)
        edit_user_and_device_mobile(driver)
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        driver.quit()

def test(case, driver):
    print("nice")


#chrome_test()
#mozilla_test()
#chrome_test_mobile()
#mozilla_test_mobile()


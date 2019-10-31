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

def shell_test(method, work_browser): 
    '''
    Это оболочка для тесоов. В качестве переменной сюда передается метод с самим кейсом
    Все завернуто в трайкетч. Eсли тест падает, запускается слудюущий метод
    Метод делает скрины при падении
    Метод пишет эксепшен
    '''

    try:
        browser = browsers()
        if work_browser == "chrome":
            driver = browser.chrome()
        if work_browser == "mozilla":
            driver = browser.mozilla()
        print (Fore.CYAN + work_browser + " test " + method.__name__ + "" + Style.RESET_ALL)
        method(driver) # вызов рабочего метода
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        browser = browsers()
        browser.close_browser(driver)
    kill_chrome_driver()

def shell_test_mobile(method, work_browser): # оболочка для chrome mobile 
    
    try:
        browser = browsers()
        if work_browser == "chrome":
            driver = browser.chrome_mobile()
        if work_browser == "mozilla":
            driver = browser.mozilla_mobile()

        print (Fore.CYAN + work_browser +  " test " + method.__name__ + "" + Style.RESET_ALL)
        method(driver) # вызов рабочего метода
    except Exception as e:
        make_screenshot(driver)
        print (Fore.LIGHTRED_EX +"###################################################")
        print (e)
        traceback.print_exc()
        time.sleep(0.2)
        print (Style.RESET_ALL)
        browser = browsers()
        browser.close_browser(driver)
    kill_chrome_driver()

def start_test_chrome_desktop (work_browser): # Метод передачи тестовых методов в рабочую оболочку

    test_list = [   # Список тестовых методов
        add_user_with_send_support, 
        edit_profile_info,
        create_user_and_devices,
        feedback_form,
        juridical_information().juridical_information,
        juridical_information().juridical_information_part2, # надо переписать для вот это для мозилы и хрома
        knowledge,
        main_page_check_unatorize,
        edit_user_and_device,
        change_password
    ] # нвоый тестовый метод добавить в конец
    
    for method in test_list: # Поселдовательный вызов всех методов
        shell_test(method, work_browser)

def start_test_chrome_mobile(work_browser): # Аналогично методу выше только для МОБИЛОК
    
    test_list = [   # Список тестовых методов
        add_user_with_send_support_mobile, 
        edit_profile_info_mobile,
        create_user_and_devices_mobile,
        feedback_form_mobile,
        juridical_information_mobile().juridical_information_mobile,
        juridical_information_mobile().juridical_information_part2_mobile,
        knowledge_mobile, 
        main_page_check_unatorize_mobile,
        edit_user_and_device_mobile,

        ##change_password Надо сделать для мобильной версии
    ] # нвоый тестовый метод добавить в конец
    
    for method in test_list: # Поселдовательный вызов всех методов
        shell_test_mobile(method, work_browser)


start_test_chrome_desktop("chrome")
start_test_chrome_mobile("chrome")
start_test_chrome_desktop("mozilla")
start_test_chrome_mobile("mozilla")

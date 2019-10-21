from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random
import names
import pyperclip
import configparser
import logging
import getpass
import re
from colorama import Fore, Style

class browsers():

    def chrome(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        d = DesiredCapabilities.CHROME
        d['goog:loggingPrefs'] = { 'browser':'ALL' }    
        driver = webdriver.Chrome(desired_capabilities=d, chrome_options=chrome_options)
        return driver

    def chrome_mobile(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=400,1000")
        d = DesiredCapabilities.CHROME
        d['goog:loggingPrefs'] = { 'browser':'ALL' }    
        driver = webdriver.Chrome(desired_capabilities=d, chrome_options=chrome_options)
        return driver

    def mozilla(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        return driver

    def mozilla_mobile(self):
        driver = webdriver.Firefox()
        driver.set_window_size(400, 1000)
        return driver

    def close_browser(self, driver):
        if driver.name == 'chrome':
            for entry in driver.get_log('browser'):
                status_print = 0
                if entry['level'] == 'DEBUG':
                    print (Fore.YELLOW + str(entry) + Style.RESET_ALL)
                    status_print = 1
                if entry['level'] == 'SEVERE':
                    print (Fore.LIGHTRED_EX + str(entry) + Style.RESET_ALL)
                    status_print = 1
                if status_print == 0:
                    print(entry)
        driver.close()

    def quit_browser(self,driver):
        if driver.name == 'chrome':
            for entry in driver.get_log('browser'):
                status_print = 0
                if entry['level'] == 'DEBUG':
                    print (Fore.YELLOW + str(entry) + Style.RESET_ALL)
                    status_print = 1
                if entry['level'] == 'SEVERE':
                    print (Fore.LIGHTRED_EX + str(entry) + Style.RESET_ALL)
                    status_print = 1
                if status_print == 0:
                    print(entry)
        driver.quit()

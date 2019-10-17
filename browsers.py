from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import names
import pyperclip
import configparser
import logging
import getpass

class browsers():

    def mozilla(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        return driver

    def chrome(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return driver

    def chrome_mobile(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=400,1000")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return driver
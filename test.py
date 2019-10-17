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
from edit_profile_info import edit_profile_info
from add_user_with_send_support import add_user_with_send_support
#test = hc_command()
#
#username = getpass.getuser()
#print(username)
#
#config = configparser.ConfigParser()
#config.read('config.ini')
#temp = config['USER INFO']['email']
#password = "23072307"
#
#chrome_options = Options()
#chrome_options.add_argument("--start-maximized")
#driver = webdriver.Chrome(chrome_options=chrome_options)
#driver.get(test.site())
#
#test.signin_parametr(driver, "829test829@gmail.com", "23072307")
#test.tariff_add(driver)
#
#driver.close()

#class someclass():
#    @log1
#    def method(self):
#        assert False

#login = '234'
#password = "few"
#print ("Info: вход с параметрами " + login + " " +  password)
#
#def log1(func):
#    def other(*args, **kwargs):
#        print ("Привет")
#        func(*args, **kwargs)
#        print ("Пока")
#        
#        return func
#    return other(func)
#
#@log1
#def some():
#    n = 1
#
#some()
#
#time.sleep(1000)


browser = browsers()
driver = browser.mozilla()
edit_profile_info(driver)


time.sleep(1)

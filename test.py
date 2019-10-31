#from selenium import webdriver 
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#import time
#import random
#import names
#import pyperclip
#from login import hc_command
#import configparser
#import logging
#import getpass
#import os
#
from browsers import browsers
#from edit_profile_info import edit_profile_info
#from add_user_with_send_support import add_user_with_send_support
#import colorama
#from colorama import Fore, Style
#import traceback
#import inspect
#from login_mobile import hc_command_mobile
#import threading

#from create_user_and_devices import create_user_and_devices

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

#
#browser = browsers()
#driver = browser.mozilla()
#edit_profile_info(driver)

#def qwe():
#
#    
#test = hc_command()
#
#try:
#    assert False
#except Exception:
#    traceback.print_exc()
#print (qwe)
#
#time.sleep(1)
#d = DesiredCapabilities.CHROME
#d['loggingPrefs'] = { 'browser':'ALL' }
#
#chrome_options = Options()
#chrome_options.add_argument("--start-maximized desired_capabilities=d")
#driver = webdriver.Chrome(chrome_options=chrome_options)

#test = hc_command()
#browser = browsers()
#driver = browser.chrome()
#driver.get(test.site())
#time.sleep(1)
#height = driver.execute_script("document.body.scrollHeight")
#print ("height = " + height)
#driver.set_window_size(1920, height)
#driver.save_screenshot("screen/save.png")
##img = driver.get_window_size()
##print (img.get('height'))
#
#driver.quit()

#create_user_and_devices(driver)

# enable browser logging
#chrome_options = Options()
#chrome_options.add_argument("--start-maximized")
#d = DesiredCapabilities.CHROME
#d['goog:loggingPrefs'] = { 'browser':'ALL' }
#driver = webdriver.Chrome(desired_capabilities=d, chrome_options=chrome_options)
#
#create_user_and_devices(driver)
##time.sleep(10)
## print messages
#for entry in driver.get_log('browser'):
#    print(entry)
#
#time.sleep(0.1)
#


# chrome --start-maximized --enable-logging=stderr

#def jui1():
#    while 0 < 1:
#        print (1)
#        time.sleep(20)
#
#def jui2():
#    while True:
#        print (2)
#        time.sleep(20)
#
#threading.Thread(target=jui1).start()
#time.sleep(0.5)
#threading.Thread(target=jui2).start()

#config = configparser.ConfigParser()
#config.read('config.ini')
#email = config['USER INFO']['email']
#password = "23072307"
#
##test = hc_command()
#config = configparser.ConfigParser()
#config.read('environment.ini')
#site = config['ENVIRONMENT']['site']
#
#
#from request_hc import request_hc
#test = hc_command()
#req = request_hc()
#req.login(test.site(), email, "23072307")   # закончил на том что возвращается dict. Что позволяет забирать токени давать его уже непосредственно в азпрсо
#
#dsa = {"qwd": "qwd12321", "qwdq": "qwdq"}
#print (dsa["qwd"])

#def odin():
#    hg = 1
#    ty = 2
#    return hg, ty
#
#asd = odin()
#print(asd)

import datetime
import psutil
import time
import calendar
#current_time = datetime.datetime.now().time()
#
#off_hour = current_time.replace(hour=12, minute=1, second=0, microsecond=0) 
#if current_time > off_hour:
#    print ("WORK WORK WORK!!!")
#else:
#    print ("Сейчас мы не работает")
#    print (current_time)

#browser = browsers()
#driver = browser.chrome()
#
#driver.get("http://front.stage.helpcubes.com")
#
#try:
#    driver.find_element_by_xpath("wfjoiwefji")
#except:
#    current_time = calendar.timegm(time.gmtime())
#    print ("screenshot crush name = " + str(current_time))
#    driver.save_screenshot("./Screenshots/" + str(current_time) + ".png")

#def odin(drink):
#    print (str(drink))
#
#def dwa(method):
#    #try:
#    
#    drink = 3
#    method(drink)
#    print (method.__name__)
#
#    #except:
#    #    print("fepo")
#
#dwa(odin)

browser = browsers()
driver = browser.mozilla()

name = driver.capabilities['browserName']
print (name)

def kill_mozilla_driver(): #
    mozilladrivername = "geckodriver.exe"
    for proc in psutil.process_iter():
        if proc.name() == mozilladrivername:
            proc.kill()

driver.get("http://foo.com")
time.sleep(1)

driver.quit()
kill_mozilla_driver()


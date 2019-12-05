from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random
import names
import pyperclip
from login import hc_command
import configparser
import logging
import getpass
import os

from browsers import browsers
from edit_profile_info import edit_profile_info
from add_user_with_send_support import add_user_with_send_support
import colorama
from colorama import Fore, Style
import traceback
import inspect
from login_mobile import hc_command_mobile
import threading
from create_user_and_devices import create_user_and_devices

import datetime
import psutil
import time
import calendar

import pytest

#browser = browsers()
#driver = browser.mozilla()
#
#name = driver.capabilities['browserName']
#print (name)
#
#def kill_mozilla_driver(): #
#    mozilladrivername = "geckodriver.exe"
#    for proc in psutil.process_iter():
#        if proc.name() == mozilladrivername:
#            proc.kill()
#
#driver.get("http://foo.com")
#time.sleep(1)
#
#driver.quit()
#kill_mozilla_driver()

@pytest.fixture()
def resource_setup(request):
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~start test~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    def resource_teardown():
        print("resource_teardown")
    request.addfinalizer(resource_teardown)

def test_pytest (resource_setup):
    browser = browsers()
    driver = browser.chrome()
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~test is runnign~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    driver.get ("https://development-prostobill-staging.k8s.bsr.group/dashboard")
    driver.find_element_by_xpath("ewfw")

def test_pytest1 (resource_setup):
    browser = browsers()
    driver = browser.chrome()
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~test is runnign~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    driver.get ("https://development-prostobill-staging.k8s.bsr.group/dashboard")

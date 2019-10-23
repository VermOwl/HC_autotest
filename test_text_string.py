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

from PIL import Image
from PIL import ImageChops

im1 = Image.open("1.png")
im2 = Image.open("2.png")

diff = ImageChops.difference(im2, im1)

diff.save("img1.png")

im = Image.open("img1.png")
pixels = im.getdata()          # get the pixels as a flattened sequence
nblack = 0
for pixel in pixels:
    if pixel < (20, 20, 20):
        nblack += 1
n = len(pixels)
percent = nblack / float(n)
print (percent)
if (nblack / float(n)) > 60:
    print("mostly black")
else:
    print("brigth")

time.sleep(1)

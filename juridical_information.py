from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import names
import pyperclip
from login import hc_command
import configparser
from browsers import browsers

class juridical_information():

    def juridical_information(self, driver):
        test = hc_command()
        driver.get(test.site())
        driver.implicitly_wait(10)

        test.open_user_agreement(driver)
        test.open_privacy_policy(driver)
        browser = browsers()
        browser.quit_browser(driver)

    def juridical_information_part2_mozilla(self, driver):
        test = hc_command()
        driver.get(test.site())
        driver.implicitly_wait(10)

        test.open_signin_form(driver)

        window_before = driver.window_handles[0]
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        time.sleep(1)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        elem = driver.find_elements_by_xpath("//a[contains(text(),'Политика конфиденциальности')]")
        elem_click = elem[0]
        elem_click.click()
        test.check_privacy_policy(driver)
        driver.switch_to.window(window_before)


        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        elem = driver.find_elements_by_xpath("//a[contains(text(),'Пользовательское соглашение')]")
        elem_click = elem[0]
        elem_click.click()
        test.check_user_agreement(driver)
        driver.switch_to.window(window_before)

        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(0.2)
        driver.find_element_by_xpath("//a[contains(text(),'Правила проведения акции')]").click()
        #elem_click = elem[0]
        #elem_click.click()
        driver.find_element_by_xpath("//li[contains(text(),'Организатор Акции ООО «Е09»')]")
        print ("Info: Правила проведения акции проверены")
        driver.switch_to.window(window_before)
        browser = browsers()
        browser.quit_browser(driver)    

    def juridical_information_part2_chrome(self, driver):
        test = hc_command()
        driver.get(test.site())
        driver.implicitly_wait(10)

        test.open_signin_form(driver)

        window_before = driver.window_handles[0]
        print ("Click: Юридические документы") 
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        print("Click: Политика конфиденциальности")
        elem = driver.find_elements_by_xpath("//a[contains(text(),'Политика конфиденциальности')]")
        elem_click = elem[0]
        elem_click.click()
        test.check_privacy_policy(driver)
        driver.switch_to.window(window_before)

        print ("Click: Юридические документы")
        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        window_after = driver.window_handles[2]
        driver.switch_to.window(window_after)
        print("Click: Пользовательское соглашение")
        elem = driver.find_elements_by_xpath("//a[contains(text(),'Пользовательское соглашение')]")
        elem_click = elem[0]
        elem_click.click()
        test.check_user_agreement(driver)
        driver.switch_to.window(window_before)
        print ("Click: Юридические документы")
        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        window_after = driver.window_handles[3]
        driver.switch_to.window(window_after)
        print("Click: Правила проведения акции")
        elem = driver.find_elements_by_xpath("//a[contains(text(),'Правила проведения акции')]")
        elem_click = elem[0]
        elem_click.click()
        driver.find_element_by_xpath("//li[contains(text(),'Организатор Акции ООО «Е09»')]")
        print ("Info: Правила проведения акции проверены")
        driver.switch_to.window(window_before)
        browser = browsers()
        browser.quit_browser(driver)

#browser = browsers()
#test = juridical_information()
#
#driver = browser.chrome()
#test.juridical_information_part2_chrome(driver)
#
#driver = browser.mozilla()
#test.juridical_information(driver)
#test.juridical_information_part2_mozilla(driver)
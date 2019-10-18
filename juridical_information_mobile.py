from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import names
import pyperclip
from login_mobile import hc_command_mobile
import configparser
from browsers import browsers


class juridical_information_mobile():

    def juridical_information_mobile(self, driver):
        test = hc_command_mobile()
        driver.get(test.site())

        time.sleep(2)
        test.open_user_agreement(driver)
        test.open_privacy_policy(driver)
        driver.quit()

    def juridical_information_part2_mozilla_mobile(self, driver):
        test = hc_command_mobile()
        driver.get(test.site())
        test.open_signin_form(driver)
        time.sleep(1)

        window_before = driver.window_handles[0]

        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        time.sleep(2)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        elem = driver.find_elements_by_xpath("//a[contains(text(),'Политика конфиденциальности')]")
        elem_click = elem[0]
        elem_click.click()
        time.sleep(1)
        test.check_privacy_policy(driver)
        driver.switch_to.window(window_before)


        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        time.sleep(1)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        elem = driver.find_elements_by_xpath("//a[contains(text(),'Пользовательское соглашение')]")
        elem_click = elem[0]
        elem_click.click()
        time.sleep(1)
        test.check_user_agreement(driver)
        driver.switch_to.window(window_before)

        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        time.sleep(2)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(1)
        elem = driver.find_elements_by_xpath("//a[contains(text(),'Правила проведения акции')]")
        elem_click = elem[0]
        elem_click.click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(text(),'Организатор Акции ООО «Е09»')]")
        print ("Info: Правила проведения акции проверены")
        driver.switch_to.window(window_before)

        driver.quit()

    def juridical_information_part2_chrome_mobile(self, driver):
        test = hc_command_mobile()
        driver.get(test.site())
        test.open_signin_form(driver)
        time.sleep(1)

        window_before = driver.window_handles[0]

        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        time.sleep(2)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        elem = driver.find_elements_by_xpath("//a[contains(text(),'Политика конфиденциальности')]")
        elem_click = elem[0]
        elem_click.click()
        time.sleep(1)
        test.check_privacy_policy(driver)
        driver.switch_to.window(window_before)


        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        time.sleep(1)
        window_after = driver.window_handles[2]
        driver.switch_to.window(window_after)
        elem = driver.find_elements_by_xpath("//a[contains(text(),'Пользовательское соглашение')]")
        elem_click = elem[0]
        elem_click.click()
        time.sleep(1)
        test.check_user_agreement(driver)
        driver.switch_to.window(window_before)

        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        time.sleep(2)
        window_after = driver.window_handles[3]
        driver.switch_to.window(window_after)
        time.sleep(1)
        elem = driver.find_elements_by_xpath("//a[contains(text(),'Правила проведения акции')]")
        elem_click = elem[0]
        elem_click.click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[contains(text(),'Организатор Акции ООО «Е09»')]")
        print ("Info: Правила проведения акции проверены")
        driver.switch_to.window(window_before)

        driver.quit()

#browser = browsers()
#test = juridical_information_mobile()
#driver = browser.chrome_mobile()
#test.juridical_information_part2_chrome_mobile(driver)

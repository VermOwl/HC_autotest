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
        driver.implicitly_wait(10)

        test.open_user_agreement(driver)
        test.open_privacy_policy(driver)
        
        browser = browsers()
        browser.quit_browser(driver)

    def juridical_information_part2_mobile(self, driver):
        # Проверяем название браузера
        # Перенаправляем на нужный метод в зависимости от браузера

        name = driver.capabilities['browserName']
        if name == "chrome":
            self.juridical_information_part2_chrome_mobile(driver)
        if name == "firefox":
            self.juridical_information_part2_mozilla_mobile(driver)
        else:
            print ("Info: Не удалось определить браузер для выполенения juridical_information_part2")
            assert False


    def juridical_information_part2_mozilla_mobile(self, driver):
        test = hc_command_mobile()
        driver.get(test.site())
        driver.implicitly_wait(10)
        test.open_signin_form(driver)

        window_before = driver.window_handles[0]
        time.sleep(0.1)
        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        time.sleep(0.2) # Наверное влкадка не успевала переключаться и поэтому драйвер не мог зацепить айдишник еще не открывшейся вкладки
        window_after = driver.window_handles[1]
        time.sleep(0.1)
        time.sleep(0.1)
        driver.switch_to.window(window_after)
        elem = driver.find_elements_by_xpath("//a[contains(text(),'Политика конфиденциальности')]")
        elem_click = elem[0]
        elem_click.click()
        test.check_privacy_policy(driver)
        driver.switch_to.window(window_before)


        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        window_after = driver.window_handles[1]
        time.sleep(0.1)
        driver.switch_to.window(window_after)
        elem = driver.find_elements_by_xpath("//a[contains(text(),'Пользовательское соглашение')]")
        elem_click = elem[0]
        elem_click.click()
        test.check_user_agreement(driver)
        driver.switch_to.window(window_before)

        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        window_after = driver.window_handles[1]
        time.sleep(0.1)
        driver.switch_to.window(window_after)
        elem = driver.find_elements_by_xpath("//a[contains(text(),'Правила проведения акции')]")
        elem_click = elem[0]
        elem_click.click()
        driver.find_element_by_xpath("//li[contains(text(),'Организатор Акции ООО «Е09»')]")
        print ("Info: Правила проведения акции проверены")
        driver.switch_to.window(window_before)
        browser = browsers()
        browser.quit_browser(driver)

    def juridical_information_part2_chrome_mobile(self, driver):
        test = hc_command_mobile()
        driver.get(test.site())
        driver.implicitly_wait(10)
        test.open_signin_form(driver)

        window_before = driver.window_handles[0]
        time.sleep(0.1)
        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        time.sleep(0.1)
        window_after = driver.window_handles[1]
        time.sleep(0.1)
        driver.switch_to.window(window_after)
        elem = driver.find_elements_by_xpath("//a[contains(text(),'Политика конфиденциальности')]")
        elem_click = elem[0]
        elem_click.click()
        test.check_privacy_policy(driver)
        driver.switch_to.window(window_before)


        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        time.sleep(0.1)
        window_after = driver.window_handles[2]
        time.sleep(0.1)
        driver.switch_to.window(window_after)
        elem = driver.find_elements_by_xpath("//a[contains(text(),'Пользовательское соглашение')]")
        elem_click = elem[0]
        elem_click.click()
        test.check_user_agreement(driver)
        time.sleep(0.1)
        driver.switch_to.window(window_before)

        driver.find_element_by_xpath("//a[contains(text(),'Юридические документы')]").click()
        time.sleep(0.1)
        window_after = driver.window_handles[3]
        time.sleep(0.1)
        driver.switch_to.window(window_after)
        time.sleep(0.2)
        print ("Info: Проверка правила првоедеения акции")
        driver.find_element_by_xpath("//a[contains(text(),'Правила проведения акции')]").click()
        driver.find_element_by_xpath("//li[contains(text(),'Организатор Акции ООО «Е09»')]")
        print ("Check: Правила проведения акции проверены")
        driver.switch_to.window(window_before)
        browser = browsers()
        browser.quit_browser(driver)

#browser = browsers()
#test = juridical_information_mobile()
#driver = browser.mozilla_mobile()
#
##test.juridical_information_mobile(driver)
#test.juridical_information_part2_chrome_mobile(driver)

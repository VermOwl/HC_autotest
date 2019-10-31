from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import names
import pyperclip
import configparser
import getpass
import os
from browsers import browsers
from colorama import Fore, Style
from request_hc import request_hc

# Print status
# Click
# Check
# Info
# Fill
#        self.wait_loss(driver, "//div[@class='nuxt-progress']")
#

class hc_command():

    mail = "qwe"

    def get_email_from_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        email = config['USER INFO']['email']
        return email

    def clear_field(self, driver, field_to_clear):
        driver.find_element_by_xpath(field_to_clear).send_keys(Keys.CONTROL + "a")
        driver.find_element_by_xpath(field_to_clear).send_keys(Keys.DELETE)

    def wait_loss(self, driver, what_wait): # Ожидает исчезновнеие серго фона, который появляется во время загрузки страницы
        # чаще всего использоуется 
        # self.wait_loss(driver, "//div[@class='nuxt-progress']")
        result = False
        driver.implicitly_wait(1.5)
        try: 
            driver.find_element_by_xpath(what_wait)
            result = False
        except:
            result = True
        if result != True:
            self.wait_loss(driver, what_wait)        
        driver.implicitly_wait(10)    

    def signin(self, driver): #логиниться на helpcubes
        
        #Войти в аккаунт
        print ("Click: Вход в аккаунт")
        driver.find_element_by_xpath("(//a[@class='btn-radius my-auto ml-4 mr-3 pl-3 pr-3 v-btn v-btn--depressed v-btn--flat v-btn--outlined v-btn--router theme--light v-size--default primary--text'])").click()

        #Заполнение формы ввода
        mail = self.__memory_mail()
        print("Fill: форма входа пользвоаель")
        driver.find_element_by_xpath("(//div[@class='v-input pt-5 theme--light v-text-field v-text-field--is-booted v-text-field--enclosed v-text-field--outlined']//input)").send_keys(mail)
        driver.find_element_by_xpath("(//input[@name='password'])").send_keys("23072307")

        #Войти
        print ("Click: Войти")
        driver.find_element_by_xpath("(//button[@class='v-btn v-btn--contained theme--light v-size--default primary'])").click()

        #Скипнуть момент добавления карты - Открывается главная страница
        print ("Скипнуть момент добавления карты - Открывается главная страница")
        try:
            driver.find_element_by_xpath("//button[@class='v-btn v-btn--depressed v-btn--flat v-btn--outlined theme--light v-size--default primary--text']").click()
        except:
            print("фывалдо")

    def setting(self, driver): #заходит в настройки пользователя
        print("Click: Настройки пользваоеля")
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//i[contains(text(),'settings')]").click()
                i = 100
            except:
                i += 1
                time.sleep(0.1)

    def setting_devices(self, driver): #открыть пользователи и устройства
        print ("Click: Открыть пользователи и устройства")
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        driver.find_element_by_xpath("//main[@class='v-content']//a[2]").click()

    def add_devices(self, driver): #добавление устройства
        print ("Info: Добавление устройство для пользователя")
        print ("Click: Добавить устройствво")
        driver.find_element_by_xpath("//div[@class='flex right-block xs-8']//div[@class='flex pt-4 mt-2']//button[@class='v-btn v-btn--contained theme--light v-size--default secondary']").click()    
        print ("Fill: Название устройства")
        name = names.get_full_name()
        driver.find_element_by_xpath("//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/div[@class='v-dialog__content v-dialog__content--active']/div[@class='v-dialog v-dialog--active v-dialog--persistent']/div[@class='v-card v-sheet theme--light']/div[@class='v-card__text']/form[@class='v-form']/div[@class='device-modal__field']/div[@class='v-input theme--light v-text-field v-text-field--is-booted v-text-field--enclosed v-text-field--outlined']/div[@class='v-input__control']/div[@class='v-input__slot']/div[@class='v-text-field__slot']/input[1]").send_keys(name)
        print ("Fill: Производитель")
        driver.find_element_by_xpath("//div[@class='flex pr-3 pa-md-0 xs12 md6']//div[@class='v-input theme--light v-text-field v-text-field--is-booted v-text-field--enclosed v-text-field--outlined']//input").send_keys(name)
        print ("Fill: Модель")
        driver.find_element_by_xpath("//div[@class='flex pl-3 pa-md-0 xs12 md6']//div[@class='v-input theme--light v-text-field v-text-field--is-booted v-text-field--enclosed v-text-field--outlined']//input").send_keys("autotest")
        # выбор типа устройства
        print ("Select: Тип устройства")
        driver.find_element_by_xpath("//div[@class='flex pr-3 pa-md-0 xs12 md6']//div[@class='v-select__selections']").click()
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//div[@class='v-menu__content theme--light v-menu__content--fixed menuable__content__active']//div[@class='v-list v-sheet v-sheet--tile theme--light']//div[1]//div[1]//div[1]").click()
                i = 200
            except Exception as e:
                print (e)
                i += 1
                time.sleep(0.1)

        #    выбор операционной систомы
        print ("Select: ОС девайса")
        driver.find_element_by_xpath("//div[@class='v-input theme--light v-text-field v-text-field--is-booted v-text-field--enclosed v-text-field--outlined v-select']//div[@class='v-select__selections']").click()
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//div[contains(text(),'Windows 10')]").click()
                i = 100
            except:
                i += 1
                time.sleep(0.1)

        # подтверждение
        print ("Select: Сохранения устройства")
        driver.find_element_by_xpath("//button[@class='device-modal__button v-btn v-btn--contained theme--light v-size--default primary']//span[@class='v-btn__content']").click()
        
        print("Site refresh")
        driver.refresh()
        
        # проверка данных
        print ("Info: Проверка добавленного устройств")
        print ("Check: Название деваса")
        driver.find_element_by_xpath("//div[@class='flex right-block xs-8']//h3[@class='title'][contains(text(),'" + name + "')]")
        print ("Check: Тип девайса")
        driver.find_element_by_xpath("//p[@class='body-1 mb-0'][contains(text(),'Настольный компьютер')]")
        print ("Check: ОС девайсас")
        driver.find_element_by_xpath("//p[@class='body-1 mb-0'][contains(text(),'Windows 10')]")
        print ("Check: Производитель девайса")
        driver.find_element_by_xpath("//p[@class='body-1 mb-0'][contains(text(),'" + name + "')]")
        print ("Check: Модель девайса")
        driver.find_element_by_xpath("//p[@class='body-1 mb-0'][contains(text(),'autotest')]")
        
        print ("Info: Устройство добавлено. Данные проверены после перезагрузки")

    def support_message(self,driver): #Заполениен формы отправки сообщения в службу поддержки
        
        print ("Info: Заполнение и отправки формы в ТП")
        #Написать в поддержку
        print ("Click: Открытие формы отправки сообщения в ТП")
        driver.find_element_by_xpath("//div[@class='text-xs-right ml-5 my-auto']//button[@class='activator-btn v-btn v-btn--contained theme--light v-size--default']").click()

        print ("Fill: Тема обращения")
        #Заполенние формы поддержки
        summary = "AUTOTEST messege in support"
        driver.find_element_by_xpath("//input[@name='name']").send_keys(summary)
        
        #Выбор категории устройства
        print ("Select: Категория обращения")
        elem_list = driver.find_elements_by_xpath("//div[@class='v-select__selections']")
        elem = elem_list[0]
        elem.click() 
        driver.find_element_by_xpath("//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/div[@class='v-menu__content theme--light v-menu__content--fixed menuable__content__active']/div[@class='v-select-list v-card theme--light']/div[@class='v-list v-sheet v-sheet--tile theme--light']/div[1]/div[1]").click()
        
        #Выбор устройства из списка
        print ("Select: Устрйоство")
        elem = elem_list[1]
        elem.click()
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/div[@class='v-menu__content theme--light v-menu__content--fixed menuable__content__active']/div[@class='v-select-list v-card theme--light']/div[@class='v-list v-sheet v-sheet--tile theme--light']/div[2]/div[1]").click()
                i = 200
            except:
                i += 1
                time.sleep(0.1)
                print (str(i))


        
        #Выбор пользователя из списка
        print ("Select: Пользователь")
        elem = elem_list[2]
        elem.click()
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/div[@class='v-menu__content theme--light v-menu__content--fixed menuable__content__active']/div[@class='v-select-list v-card theme--light']/div[@class='v-list v-sheet v-sheet--tile theme--light']/div[2]/div[1]").click()
                i = 100
            except:
                i += 1
                time.sleep(0.1)
        
        #Добавление комментария
        print ("Fill: Описание проблемы")
        description = "Lorem ipsum dolor sit amet"
        driver.find_element_by_xpath("//textarea[@name='comment']").send_keys("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.")
        
        #Добавление файла
        print ("Fill: Добавление файла")
        driver.find_element_by_xpath("//input[@name='files[]']").send_keys(os.getcwd() + "\\ford-ford-raptor-parketnik-dzhip.jpeg")
        
        #Нажатие кнопки отправить
        print ("Click: Отправить запрос в ТП")
        driver.find_element_by_xpath("//button[@class='v-btn v-btn--contained theme--light v-size--default primary']").click()

        self.check_request_jira_authorization(summary, description)

        print ("Info: Открыта страница с запросами - проверка наличие запроса")
        print ("Check: Тема запроса")
        driver.find_element_by_xpath("//h6[contains(text(),'" + summary + "')]")
        print ("Check: Описание запроса")
        driver.find_element_by_xpath("//p[contains(text(),'" + description + "')]")
        print ("Check: Наличие файла в запросе")
        driver.find_element_by_xpath("//div[@class='v-avatar v-avatar--tile']//span//a//img")

        print("Info: Запрос в ТП успешно отправлен")
        #Добавить чек на то что какая открылась страница
        
    def registration(self, driver): #Регситрация пользвоателя 
        print ("Info: Процедура регистрации пользователя")
        print ("Click: Регистрация")
        #Неавторизованный пользовать - Регистрация
        driver.find_element_by_xpath("(//a[@class='btn-radius my-auto v-btn v-btn--contained v-btn--router theme--light v-size--default primary'])").click()

        #Заполняется форма регистрации
        print ("Fill: Ваше имя")
        name = names.get_first_name()
        driver.find_element_by_xpath("(//div[@class='v-input pt-5 theme--light v-text-field v-text-field--is-booted v-text-field--enclosed v-text-field--outlined']//input)[1]").send_keys(name)
        mail = self.__memory_mail()
        print ("Fill: Email")        
        driver.find_element_by_xpath("(//div[@class='v-input theme--light v-text-field v-text-field--is-booted v-text-field--enclosed v-text-field--outlined']//input)[1]").send_keys(mail)
        print ("Fill: Пароль")
        driver.find_element_by_xpath("(//div[@class='flex xs12']//div[@class='v-input pt-3 theme--light v-text-field v-text-field--is-booted v-text-field--enclosed v-text-field--outlined']//input)[1]").send_keys("23072307")
        print ("Fill: Повторить пароль")
        driver.find_element_by_xpath("(//div[@class='flex']//input)[1]").send_keys("23072307")

        #Политика конфиденциальности - Зарегистрироваться
        print ("Click: Чекбокс соглашения пользователя")
        driver.find_element_by_xpath("//div[@class='v-input--selection-controls__ripple']").click()
        print ("Click: Зарегистрироваться")
        driver.find_element_by_xpath("(//button[@class='v-btn v-btn--contained theme--light v-size--default primary'])").click()
        time.sleep(0.5) #Добавил потомучто перестало выходить на главную страницу
        #выход на главную
        driver.find_element_by_xpath("(//button[@class='v-btn v-btn--contained theme--light v-size--default primary'])").click()
        driver.find_element_by_xpath("(//button[@class='v-btn v-btn--contained theme--light v-size--default primary'])").click()


    def getmail(self, driver): #Копируем в буфер аккаунт с сайта temp-mail.org
        print ("Click: Копирование текста в буфер обмена")
        driver.find_element_by_xpath("//button[@class='btn-rds icon-btn bg-theme click-to-copy copyIconGreenBtn']").click()
        self.__memory_mail()

    def confirm_mail(self, driver): #Подтвердить email
        i = 0 
        print ("Info: Переход по ссылке")
        while i < 10:
            try:
                time.sleep(1)
                driver.find_element_by_xpath("//span[contains(text(),'Helpcubes |')]").click()
                time.sleep(1)
                driver.execute_script("window.scrollTo(0, 1080)") 
                time.sleep(0.5)
                driver.find_element_by_xpath("//a[@class='link']").click()
                time.sleep(1)  
                break
            except:
                i += 1  
                        
    def __memory_mail(self): #Хранилка email'а
        mail = pyperclip.paste()
        return mail

    def tariff_add(self, driver): #Добавиление тарифа
        #Раздел: Тарифы
        print ("Info: Добавления тариф для пользователя")
        print ("Click: Тарифы")
        driver.find_element_by_xpath("//span[@class='v-btn__content'][contains(text(),'Тарифы')]").click()

        #Выбрать второй тариф максимальный
        print ("Click: Выбрать тариф")
        elem_list = driver.find_elements_by_xpath("//button[@class='primary v-btn v-btn--contained theme--light v-size--default']//span[contains(text(),'Выбрать')]")
        elem = elem_list[2]
        elem.click()

        #Заполнить информацию о карте
        print ("Info: Заполениение информации о карте")
        elem_list = driver.find_elements_by_xpath("//input[@type='text']")
        elem = elem_list[1]
        print ("Fill: Номер карты")
        elem.send_keys("4242424242424242")
        elem = elem_list[2]
        print ("Fill: Cardholer name")
        elem.send_keys("AUTOTEST SELENIUM")
        elem = elem_list[3]
        print ("Fill: Срок действия карты")
        elem.send_keys("1235")
        elem = elem_list[4]
        print ("Fill: СVV")
        elem.send_keys("321")

        #Подтвердить оплату
        print ("Click: Оптатить")
        driver.find_element_by_xpath("//button[@class='v-btn v-btn--contained theme--light v-size--default']").click()

    def signin_parametr(self, driver, login, password): #Вход со своими параметрами 
        
        print ("Info: вход с параметрами " + login + " " +  password)
        #Войти в аккаунт
        print ("Click: Вход в аккаунт")
        driver.find_element_by_xpath("(//a[@class='btn-radius my-auto ml-4 mr-3 pl-3 pr-3 v-btn v-btn--depressed v-btn--flat v-btn--outlined v-btn--router theme--light v-size--default primary--text'])").click()

        #Заполнение формы ввода
        print ("Fill: mail")
        driver.find_element_by_xpath("(//div[@class='v-input pt-5 theme--light v-text-field v-text-field--is-booted v-text-field--enclosed v-text-field--outlined']//input)").send_keys(login)
        print ("Fill: pass")
        driver.find_element_by_xpath("(//input[@name='password'])").send_keys(password)

        #Войти
        print ("Click: Вход после заполения полей")
        driver.find_element_by_xpath("(//button[@class='v-btn v-btn--contained theme--light v-size--default primary'])").click()

        #Скипнуть момент добавления карты - Открывается главная страница
        try:
            driver.implicitly_wait(2)
            driver.find_element_by_xpath("(//div[@class='logo']//img)").click()
            driver.implicitly_wait(10)
        except:
            print("фывалдо")
            driver.implicitly_wait(10)

    def add_profile_info(self, driver): #Заполнение информации о пользваотеле
        print ("Info: заполнение основной информации о пользователе")
        # Добавление фотки
        print ("Fill: Добавление фотки")
        driver.find_element_by_xpath("//input[@type='file']").send_keys(os.getcwd() + "\\ford-ford-raptor-parketnik-dzhip.jpeg")
        # Изменение фамилии
        print ("Fill: Добавление фамилии")
        last_name = names.get_last_name()
        driver.find_element_by_xpath("//input[@name='last_name']").send_keys(last_name)
        # Вставка дату рождения
        print ("Fill: Заполнение даты рождения")
        dateofbirth = "14.04.1986"
        driver.find_element_by_xpath("//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/div[@class='application--wrap']/main[@class='v-content']/div[@class='v-content__wrap']/div[@class='account-bg']/div[@class='container pa-xs-0']/div[@class='layout wrap']/div[@class='flex right-block xs12 md8']/div[@class='bg-xs-white']/form[@id='form']/div[@class='mx-auto v-card v-sheet v-sheet--tile theme--light']/div[@class='v-card__text pt-xs-0 px-xs-4']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys(dateofbirth)
        # Женский пол
        print ("Click: Установить женский пол")
        elem = driver.find_elements_by_xpath("//div[@class='v-input--selection-controls__ripple']")
        elem_click = elem[1]
        elem_click.click()
        # Изменение номера телефона
        print ("Fill: Установить номер телефона")
        time.sleep(0.5)
        driver.find_element_by_xpath("//input[@placeholder='+7 (###) ###-##-##']").send_keys("1234567890")     
        # Сохранить изменения
        time.sleep(0.5)
        print ("Click: Сохранить")
        driver.find_element_by_xpath("//button[@class='v-btn v-btn--contained theme--light v-size--default primary']//span[@class='v-btn__content']").click()
        # Обновить страницу
        time.sleep(0.2)
        driver.refresh()
        # Проверка изменений 
        print ("Info: Проверка добаленной информации")
        print ("Check: Фамилия")
        driver.find_element_by_xpath("//input[@value='" + last_name + "']")
        print ("Check: Пол")
        driver.find_element_by_xpath("//div[@class='v-radio theme--light v-item--active']//input[@value='female']")
        print ("Check: Номер телефона")
        driver.find_element_by_xpath("//input[@value='+7 (123) 456-78-90']")

    def add_user(self, driver): #добавление юзера в настройках пользователя
        #Открыть форму добавления пользвоателя
        print ("Info: Добавление юзера в аккаунт пользователя")
        print ("Click: Добавить пользователя")
        driver.find_element_by_xpath("//div[@class='flex right-block xs-8']//div[@class='flex pt-4 mt-2 pb-2']//button[@class='v-btn v-btn--contained theme--light v-size--default secondary']").click()

        #Заполнение полей Имя, Пол, номер, Email, Telegram, Skype
        name = names.get_first_name()
        print ("Fill: Добавить имя юзера")
        driver.find_element_by_xpath("//div/input[@aria-label='Имя']").send_keys(name)
        print ("Click: Пол юзера")
        driver.find_element_by_xpath("//div[@class='v-input--selection-controls__ripple']").click()
        print ("Fill: Номер телефона юзера")
        driver.find_element_by_xpath("//input[@placeholder='+7 (###) ###-##-##']").send_keys("1234567890")
        print ("Fill: Мыло юзера")
        mail = "autotestemail"+ str(random.randint(1000000, 9999999)) + "@python.org"
        driver.find_element_by_xpath("//input[@aria-label='Email']").send_keys(mail)
        print ("Fill: телега юзера")
        driver.find_element_by_xpath("//input[@aria-label='Telegram']").send_keys("HelpcubesTelegramAutotest")
        print ("Fill: скайп юзера")
        driver.find_element_by_xpath("//input[@aria-label='Skype']").send_keys("HelpCubesSkypeAutotest")
        #Сохранить изменения 
        print ("Click: Сохранить изменения")
        driver.find_element_by_xpath("//button[@class='users-modal__button v-btn v-btn--contained theme--light v-size--default primary']").click()
        
        driver.refresh()

        # Проверка полей
        print("Check: Имя юзера")
        driver.find_elements_by_xpath("//div[@class='user-card v-card v-sheet v-sheet--tile theme--light']//h3[@class='title'][contains(text(),'" + name + "')]")
        print("Check: номер телефона юзера")
        driver.find_element_by_xpath("//div[@class='flex right-block xs-8']//p[@class='body-1 mb-0'][contains(text(),'+7 (123) 456-78-90')]")
        print("Check: мыло юзера")
        driver.find_element_by_xpath("//div[@class='flex right-block xs-8']//p[@class='body-1 mb-0'][contains(text(),'" + mail + "')]")
        print("Check: телега юзера")
        driver.find_element_by_xpath("//div[@class='flex right-block xs-8']//p[@class='body-1 mb-0'][contains(text(),'HelpcubesTelegramAutotest')]")
        print("Check: скайп юзера")
        driver.find_element_by_xpath("//div[@class='flex right-block xs-8']//p[@class='body-1 mb-0'][contains(text(),'HelpCubesSkypeAutotest')]")
        
        print ("Пользователь добавлен в аккаунт. Данные проверены после перезагрузки")

    def setting_credit_card(self, driver): #Открыть Платежная информация
        time.sleep(1)
        #Настройки - Платежная инфомрация
        print ("Info: Открытие платежной информации в настройках пользователя")
        print ("Click: Платежная инфомрация")
        driver.find_element_by_xpath("//i[contains(text(),'credit_card')]").click()
        time.sleep(1)

    def cahnge_renew(self, driver): #Выключить автопродление 
        print("Info: Работа автопродления подписки")
        time.sleep(1)
        #Выключаем автопродление
        print ("Click: Выклюить автопродление")
        driver.find_element_by_xpath("//div[@class='v-input--selection-controls__ripple accent--text']").click()
        time.sleep(0.5)
        driver.refresh()
        time.sleep(2)
        #Проверяем выключился ли он
        print ("Check: Автопродление выключено")
        driver.find_element_by_xpath("//input[@aria-checked='false']")
        #Включаем автопродление 
        print ("Check: Включить автопродление")
        driver.find_element_by_xpath("//div[@class='v-input--selection-controls__ripple']").click()
        time.sleep(0.5)
        driver.refresh()
        time.sleep(2)
        # Проверяем включился ли он
        print ("Check: Автопродление включено")
        driver.find_element_by_xpath("//input[@aria-checked='true']")
        
        print ("Info: Автопродлены выключен и затем включены. Проведены проверки после преезагрузок")

    def payment_method_change(self, driver, card_number, card_holder, time_card, cvv): 
        time.sleep(1)

        # Редактирование карты
        driver.find_element_by_xpath("//i[contains(text(),'create')]").click()

        # Изменение номера карты
        driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field vuetify-pay-form__field_number']//input").send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field vuetify-pay-form__field_number']//input").send_keys(card_number)

        # Изменение кардхолдер нейм
        driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field vuetify-pay-form__field_holder']//input").clear()
        driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field vuetify-pay-form__field_holder']//input").send_keys(card_holder)

        # Изменение даты
        driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field-expire']//input").clear()
        driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field-expire']//input").send_keys(time_card)

        # Изменение CVV
        driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field-cvv']//input").clear()
        driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field-cvv']//input").send_keys(cvv)

        # Сохранить изменения 
        driver.find_element_by_xpath("//button[@class='v-btn v-btn--contained theme--light v-size--default primary']").click()
        
        print("Данные о карте изменены")

        time.sleep(1)
        driver.refresh()
        time.sleep(2)

        # Проверка последних цифр и дейсвтия карты
        driver.find_element_by_xpath("//h3[contains(text(),'**** **** **** " + card_number[-4:] + "')]")
        driver.find_element_by_xpath("//span[contains(text(),'" + time_card[2:]  + "/20" + time_card[-2:] + "')]")

        # Открыть редактирование и проверить кардхолдера
        driver.find_element_by_xpath("//i[contains(text(),'create')]")
        driver.find_element_by_xpath("//div[@value='" + card_holder + "']")

        #Сохранить изменения
        driver.find_element_by_xpath("//button[@class='v-btn v-btn--contained theme--light v-size--default primary']").click()

    def payment_method_change_delete_add(self, driver): # Отредактировать, удалить, добавить Способ оплаты
        time.sleep(1)

        # Редактирование карты
        driver.find_element_by_xpath("//i[contains(text(),'create')]").click()

        # Изменение номера карты
        i = 0
        while i < 20:
            driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field vuetify-pay-form__field_number']//input").send_keys(Keys.BACKSPACE)
            i = i + 1
        driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field vuetify-pay-form__field_number']//input").send_keys("5555555555554444")

        # Изменение кардхолдер нейм
        i = 0
        while i < 40:
            driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field vuetify-pay-form__field_holder']//input").send_keys(Keys.BACKSPACE)
            i = i + 1
        driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field vuetify-pay-form__field_holder']//input").send_keys("selenium cardholder")

        # Изменение даты
        i = 0 
        while i < 6:
            driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field-expire']//input").send_keys(Keys.BACKSPACE)
            i = i + 1 
        driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field-expire']//input").send_keys("0131")

        # Изменение CVV
        i = 0
        while i < 4:
            driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field-cvv']//input").send_keys(Keys.BACKSPACE)
            i = i + 1
        driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field-cvv']//input").send_keys("534")

        # Сохранить изменения 
        driver.find_element_by_xpath("//button[@class='v-btn v-btn--contained theme--light v-size--default primary']").click()
        
        print("Данные о карте изменены")

        time.sleep(1)
        driver.refresh()
        time.sleep(2)

        # Проверка последних цифр и дейсвтия карты
        driver.find_element_by_xpath("//h3[contains(text(),'**** **** **** 4444')]")
        driver.find_element_by_xpath("//span[contains(text(),'01/2031')]")
        
        # Открыть редактирование и проверить кардхолдера
        driver.find_element_by_xpath("//i[contains(text(),'create')]").click()
        driver.find_element_by_xpath("//div[@value='SELENIUM CARDHOLDER']")

        # Удалить карту - подтвердить
        driver.find_element_by_xpath("//button[@class='v-btn v-btn--flat v-btn--text theme--light v-size--default error--text']//span[@class='v-btn__content']").click()
        time.sleep(1.5)
        driver.find_element_by_xpath("//button[@class='v-btn v-btn--contained theme--light v-size--default red-gradient']//span[@class='v-btn__content']").click()

        time.sleep(1)
        driver.refresh()
        time.sleep(2)


        # Проверить отсутсвие карты 
        try:
            driver.find_element_by_xpath("//h3[contains(text(),'**** **** **** 4444')]")
        except:
            i = 1

        if i != 1:
            assert False

        time.sleep(1)

        # Редактирование карты
        driver.find_element_by_xpath("//i[contains(text(),'create')]").click()

        # Изменение номера карты
        i = 0
        while i < 20:
            driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field vuetify-pay-form__field_number']//input").send_keys(Keys.BACKSPACE)
            i = i + 1
        driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field vuetify-pay-form__field_number']//input").send_keys("5555555555554444")

        # Изменение кардхолдер нейм
        i = 0
        while i < 40:
            driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field vuetify-pay-form__field_holder']//input").send_keys(Keys.BACKSPACE)
            i = i + 1
        driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field vuetify-pay-form__field_holder']//input").send_keys("selenium cardholder")

        # Изменение даты
        i = 0 
        while i < 6:
            driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field-expire']//input").send_keys(Keys.BACKSPACE)
            i = i + 1 
        driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field-expire']//input").send_keys("0131")

        # Изменение CVV
        i = 0
        while i < 4:
            driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field-cvv']//input").send_keys(Keys.BACKSPACE)
            i = i + 1
        driver.find_element_by_xpath("//div[@class='vuetify-pay-form__field-cvv']//input").send_keys("534")

        # Сохранить изменения 
        driver.find_element_by_xpath("//button[@class='v-btn v-btn--contained theme--light v-size--default primary']").click()
        
        print("Данные о карте изменены")

        time.sleep(1)
        driver.refresh()
        time.sleep(2)

        # Проверка последних цифр и дейсвтия карты
        driver.find_element_by_xpath("//h3[contains(text(),'**** **** **** 4444')]")
        driver.find_element_by_xpath("//span[contains(text(),'01/2031')]")
        
        # Открыть редактирование и проверить кардхолдера
        driver.find_element_by_xpath("//i[contains(text(),'create')]").click() 
        time.sleep(1)
        driver.find_element_by_xpath("//div[@value='SELENIUM CARDHOLDER']")

        # Сохранить изменения 
        driver.find_element_by_xpath("//button[@class='v-btn v-btn--contained theme--light v-size--default primary']").click()
        time.sleep(1)

    def feedback_form(self, driver): #Форма обратной свзяи

        print ("Info: Проверка заполнения и отправки Формы обратной связи")
        # Открыть контакты
        print ("Click: Открыть страницу Контакты")
        time.sleep(0.2)
        driver.find_element_by_xpath("//a[@class='v-btn v-btn--flat v-btn--router v-btn--text theme--light v-size--default']//span[contains(text(),'Контакты')]").click() 

        # Заполнение полей Имя, номера телефона, мыло, сообщение
        name = names.get_full_name()
        print ("Fill: Имя")
        driver.find_element_by_xpath("//input[@aria-label='Ваше имя']").send_keys(name)
        print ("Fill: Номер телефона")
        phone = "1234567890"
        driver.find_element_by_xpath("//input[@aria-label='Номер телефона']").send_keys(phone)
        print ("Fill: mail")
        mail = "autotestemail"+ str(random.randint(1000000, 9999999)) + "@python.org"
        driver.find_element_by_xpath("//input[@aria-label='Email']").send_keys(mail)
        print ("Fill: Описание запрса")
        description = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit."
        driver.find_element_by_xpath("//textarea[@aria-label='Ваше сообщение']").send_keys(description)
        
        # Отправить запрос 
        print ("Click: Отправить запрос")
        driver.find_element_by_xpath("//button[@type='submit']").click()

        self.chech_request_jira(mail, phone, name, description)
        
        # Кнопка Спассибо
        print ("Click: Спасибо")
        driver.find_element_by_xpath("//button[@class='green-btn text-xs-left v-btn v-btn--contained theme--light v-size--default']").click()

        print("Отправка запроса по форме отбраной связи успешно завершена")        

    def chech_request_jira(self, mail, phone, name, description): #Проверка на приход информации в jira при запросе в ТП от неавторизованного пользвоателя
        
        print("Info: Запущена проверка прихода запросов в JIRA")
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://jira.bsr.group/projects/CSUP/queues/custom/")
        driver.implicitly_wait(10)

        # Вход в аккаунт
        print ("Fill: Логин Jira")
        driver.find_element_by_xpath("//input[@id='login-form-username']").send_keys("vermowl")
        print ("Fill: Пароль Jira")
        driver.find_element_by_xpath("//input[@id='login-form-password']").send_keys("9575344GHty")
        print ("Click: Логин")
        driver.find_element_by_xpath("//input[@id='login-form-submit']").click()

        # Открытие первой найденной задачи 
        print ("Click: Открытие первой найденной задачи")
        elem = driver.find_elements_by_xpath("//a[@class='issue-link']")
        elem_click = elem[0]
        elem_click.click()

        # Проверка контента 
        print ("Check: mail")
        driver.find_element_by_xpath("//a[contains(text(),'" + mail + "')]")
        print ("Check: phone number")
        driver.find_element_by_xpath("//div[contains(text(),'+7 (123) 456-78-90')]")
        print ("Check: Name")
        driver.find_element_by_xpath("//div[contains(text(),'" + name + "')]")
        print ("Check: Description")
        driver.find_element_by_xpath("//p[contains(text(),'" + description + "')]")
        print("Info: Запросы успешно найден и проверен в JIRA")
        driver.quit()

    def check_request_jira_authorization(self, summary, description): #Проверка на приход заявок в JIRA от авторизованног пользователя 
        
        print("Info: Запущена проверка прихода запросов в JIRA от авторизованного пользователя")

        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://jira.bsr.group/projects/CSUP/queues/custom/")
        driver.implicitly_wait(10)

        # Вход в аккаунт
        print ("Fill: Логин Jira")
        driver.find_element_by_xpath("//input[@id='login-form-username']").send_keys("vermowl")
        print ("Fill: Пароль Jira")
        driver.find_element_by_xpath("//input[@id='login-form-password']").send_keys("9575344GHty")
        print ("Click: Логин")
        driver.find_element_by_xpath("//input[@id='login-form-submit']").click()

        # Открытие первой найденной задачи 
        print ("Click: Открытие первой найденной задачи")
        elem = driver.find_elements_by_xpath("//a[@class='issue-link']")
        elem_click = elem[0]
        elem_click.click()

        # Проверка контента
        print ("Check: Название запроса")
        driver.find_element_by_xpath("//h1[contains(text(),'" + summary + "')]")
        print ("Check: Описание запроса")
        driver.find_element_by_xpath("//p[contains(text(),'" + description + "')]")
        print ("Check: Прикрепленный файл")
        driver.find_element_by_xpath("//div[@class='attachment-thumb']//a//img")

        print ("Info: Запрос от авторизованного пользователя найден")
        driver.quit()

    def open_signin_form(self,driver):   #Открыть форму входа пользователя
        print ("Info: Открыть форму логина")
        print ("Click: Вход")
        driver.find_element_by_xpath("//span[@class='v-btn__content'][contains(text(),'Вход')]").click()

    def open_registration_form(self,driver): #Окткрыть форму регистрациии пользвоателя
        time.sleep(1)
        print ("Info: Открыть форму регистрации польвателя")
        print ("Click: Регистрация")
        driver.find_element_by_xpath("//span[@class='v-btn__content'][contains(text(),'Регистрация')]").click()
        time.sleep(1)

    def open_user_agreement(self, driver): #Открыть страницу пользвоательского соглашения
        time.sleep(1)
        print ("Info: Открыть страницу пользвоательского соглашения")
        window_before = driver.window_handles[0]
        print ("Click: Политика конфиденциальности")
        driver.find_element_by_xpath("//a[@target='_blank'][contains(text(),'Политика конфиденциальности')]").click()
        time.sleep(1)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        self.check_user_agreement(driver)
        driver.switch_to_window(window_before)

    def check_user_agreement(self, driver): #Проверить контент страницы пользовательского соглашения
        print ("Check: Пользвоательское соглашение проверены")
        driver.find_elements_by_xpath("//li[contains(text(),'Предоставляя услуги сайта Администрация,')]")
        
        
    def open_privacy_policy(self, driver): #Открыть форму политики кионфиденкиальности
        time.sleep(1)
        print ("Info: Октрыть страницу политики конфиденциальности пользователя")
        window_before = driver.window_handles[0]
        print ("Click: Пользовательское соглашение")
        driver.find_element_by_xpath("//a[@target='_blank'][contains(text(),'Пользовательское соглашение')]").click()
        time.sleep(1)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        self.check_privacy_policy
        driver.switch_to_window(window_before)

    def check_privacy_policy(self, driver): #Проверить форму полититки конфиденциальности
        print ("Check: Политики конфиденциальности проверены")
        driver.find_element_by_xpath("//li[contains(text(),'1.6. Действие настоящих Прави')]")
        

    def site(self):
        config = configparser.ConfigParser()
        config.read('environment.ini')
        site = config['ENVIRONMENT']['site']
        return site

    def knowledge_search_field(self, driver): # Проверка строки поиска
        print ("Info: Проверка базы знаний")
        print ("Click: Раздле Windows")
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        elem = driver.find_elements_by_xpath("//div[@class='tag-items__item']")
        elem[0].click()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")

        print ("Info: Берем 4 тему")
        elem = driver.find_elements_by_xpath("//div[@class='pop-card__title']")
        elem_click = elem[3]
        theme = elem_click.text
        
        def __search_check(theme, driver):
            print ("Fill: Поле поиска: Поиск по ранее найденной 4 теме")
            time.sleep(0.2) # Наверное элемент появлялеся но еще не являлся рабочим поэтому падал
            driver.find_element_by_xpath("//input[@aria-label='Что вы хотите узнать?']").send_keys(theme)
            print ("Click: Найти")
            driver.find_element_by_xpath("//button[@class='v-btn v-btn--contained theme--light v-size--default']").click()
            self.wait_loss(driver, "//div[@class='nuxt-progress']")

            print ("Check: Найден тольк один элемент. Иначе падаем")
            elem = driver.find_elements_by_xpath("//div[@class='layout pop-card mt-3 wrap justify-center']")
            ex = 0
            try:
                elem_click = elem[1]
                ex = 1
            except:
                pass
            if ex == 1:
                assert False
            print ("Click: Сбросить")
            driver.find_element_by_xpath("//button[@class='reset v-btn v-btn--flat v-btn--text theme--light v-size--default']").click()
            self.wait_loss(driver, "//div[@class='nuxt-progress']")
            print ("Check: Отображаются все результаты поиска")
            elem = driver.find_elements_by_xpath("//div[@class='pop-card__title']")
            elem_click = elem[10]
        
        __search_check(theme, driver)
        print ("Click: База знаний")
        driver.find_element_by_xpath("//div[@class='v-toolbar__items hidden-xs']//a[@class='v-btn--active v-btn v-btn--flat v-btn--router v-btn--text theme--light v-size--default']").click()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        
        __search_check(theme, driver)
        print ("Click: База знаний")
        driver.find_element_by_xpath("//div[@class='v-toolbar__items hidden-xs']//a[@class='v-btn--active v-btn v-btn--flat v-btn--router v-btn--text theme--light v-size--default']").click()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        

    def tag_filter(self,driver): #Проверка работы плиток и нахождение тэгов в Базе знаний
        print ("Info: Проверка тэгов (Плитка)")
        print ("Check: Нахождение всех плиток")
        test_item = driver.find_elements_by_xpath("//div[@class='tag-items__item']")
        i = 0
        for elem_click in test_item:
            test_item = driver.find_elements_by_xpath("//div[@class='tag-items__item']")
            tile = test_item[i].text

            print ("Click: Плитка - " +  tile)
            test_item[i].click()
            self.wait_loss(driver, "//div[@class='nuxt-progress']")


            print ("Check: Кол-во тэгов = кол-во отображаемых тем")
            check_elem = driver.find_elements_by_xpath("//div[@class ='pop-card hidden-xs']")
            check_elem2 = driver.find_elements_by_xpath("//span[@class='caption chips'][contains(text(),'" + tile + "')]")
            if len(check_elem) != len(check_elem2)/2:
                print ("Info: Не совпало - Падаем")
                assert False
                
            print ("Check: Активный элемент справой стороны")
            check = driver.find_element_by_xpath("//div[@class='v-list-item v-list-item--link theme--light active-item']//span[@class='body-1']").text
            if check != tile:
                print ("Info: Название не подсвечено справа - падаем")
                print (check)
                print (tile)
                assert False
            print ("Click: База знаний")
            driver.find_element_by_xpath("//div[@class='v-toolbar__items hidden-xs']//a[@class='v-btn--active v-btn v-btn--flat v-btn--router v-btn--text theme--light v-size--default']").click()
            self.wait_loss(driver, "//div[@class='nuxt-progress']")
            i = i + 1


    def popular_article(self, driver): # Проверка популярных записей в Базе знаний
        print ("Info: Проверка популярных сайтов")
        print ("Check: Популярные записи")
        driver.find_element_by_xpath("//div[@class='grey-bg']//div[@class='container py-5']//p[@class='headline'][contains(text(),'Популярные')]")
        print ("Check: 5 элементов в разделе Популярные записи")
        size = len(driver.find_elements_by_xpath("//div[@class='grey-bg']//div[@class='container py-5']//div[@class='pop-card hidden-xs']"))
        if size != 5:
            print (Fore.RED + "Info: Кол-во записей не равное 5 в разделе Популярные записи - Падаем" + Style.RESET_ALL)
            assert False
        print ("Check: 5 элментов в разделе Последние добавленные записи")
        driver.find_element_by_xpath("//div[@class='white-bg']//div[@class='container py-5']//p[@class='headline'][contains(text(),'Последние добавленные записи')]")
        size = len(driver.find_elements_by_xpath("//div[@class='white-bg']//div[@class='container py-5']//div[@class='pop-card hidden-xs']"))

        
    def change_rating (self,driver): #Проверка возможности поставить голоса за или против
        print ("Info: Добавить рейтинг статье") #
        ratings = driver.find_elements_by_xpath("//p[@class='body-1 mb-0 py-1 text-xs-center']")
        rating = ratings[1].text
        rating_int = int(rating) + 1 
        print ("Click: Лайкнуть статью")
        up_rating_buttons = driver.find_elements_by_xpath("//button[@class='btn-prev v-btn v-btn--depressed v-btn--fab v-btn--flat v-btn--outlined v-btn--round v-btn--text theme--light v-size--default']")
        up_rating_buttons[1].click()
        driver.refresh()
        check_rating = driver.find_elements_by_xpath("//p[@class='body-1 mb-0 py-1 text-xs-center']")
        print ("Check: У статьи выше рейтинг?")
        if str(check_rating[1].text) == str(rating_int):
            print ("Info: Кол-во голосов неверное - падаме")
            assert False
        print ("Chekc: Изменения цвета кнопки изменения рейтинга")

        print ("Info: Отнять рейтинг у статьи") #
        ratings = driver.find_elements_by_xpath("//p[@class='body-1 mb-0 py-1 text-xs-center']")
        rating = ratings[3].text
        rating_int = int(rating) - 1 
        print ("Click: Лайкнуть статью")
        up_rating_buttons = driver.find_elements_by_xpath("//button[@class='btn-next v-btn v-btn--depressed v-btn--fab v-btn--flat v-btn--outlined v-btn--round v-btn--text theme--light v-size--default']")
        up_rating_buttons[3].click()
        driver.refresh()
        check_rating = driver.find_elements_by_xpath("//p[@class='body-1 mb-0 py-1 text-xs-center']")
        print ("Check: У статьи выше рейтинг?")
        if str(check_rating[3].text) == str(rating_int):
            print ("Info: Кол-во голосов неверное - падаме")
            assert False
        print ("Chekc: Изменения цвета кнопки изменения рейтинга")

    def chips_and_link_test (self, driver): #Проверка чипсов в Базе знаний
        print ("Info: Проверка Chips и линки Показать все")
        print ("Click: По чипсе")
        chips = driver.find_elements_by_xpath("//span[@class='caption chips']")
        chips_text = chips[1].text
        chips[1].click()
        print ("Check: Активный элемент справой стороны " + str(chips_text))
        check = driver.find_element_by_xpath("//div[@class='v-list-item v-list-item--link theme--light active-item']//span[@class='body-1']").text
        if check != chips_text:
            print ("Info: Название не подсвечено справа - падаем")
            print (check)
            print (chips_text)
            assert False
        driver.back()
        time.sleep(0.2)
        print ("Click: По Показать все")
        driver.find_element_by_xpath("//div[@class='grey-bg']//div//a[@class='view-all']").click()
        print ("Check: Активный элемент справой стороны Все статьи")
        check = driver.find_element_by_xpath("//div[@class='v-list-item v-list-item--link theme--light active-item']//span[@class='body-1']").text
        if check != "Все статьи":
            print ("Info: Название не подсвечено справа - падаем")
            print (check)
            print (chips_text)
            assert False

        driver.back()
        time.sleep(0.2)
        self.wait_loss(driver, "//div[@class='nuxt-progress']")


    def copy_link_to_article (self, driver): #Првоеряет работу линков с чипсы Поделиться
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        print ("Info: Проверка работы Копирвоание ссылки для статьи в Базе щнаний")
        title_before = driver.find_elements_by_xpath("//div[@class='pop-card__title']")[0].text
        print ("Click: Поделиться ссылкой")
        driver.find_elements_by_xpath("//button[@class='pop-btn v-btn v-btn--contained theme--dark v-size--default']")[1].click()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        
        print ("Click: Копировать ссылку")
        driver.find_element_by_xpath("//div[@class='pop__copy v-list-item theme--light']//a").click()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")

        print ("Переход по ссылке")
        driver.get(pyperclip.paste())
        print ("Check: Правильная открылась статья?")
        title_after = driver.find_element_by_xpath("//h1[@class='card-full__title display-1']").text
        if title_after != title_before:
            print("Info: Статьи не совпали - падаем")
            assert False
        driver.back()
        time.sleep(0.2)
        self.wait_loss(driver, "//div[@class='nuxt-progress']")


    def main_page_check (self, driver): #Наличия контента на главной странице helpcybes
        
        print ("Info: Проверка главной страицы Helpcubes")
        print ("Check: Круглосуточная эксперная техническая поддеркжа")
        driver.find_element_by_xpath("//h1[@class='display-3'][contains(text(),'Круглосуточная')]")
        print ("Check: Комманда профессионалов, ...")
        driver.find_element_by_xpath("//p[@class='body-1 pt-5 mt-2'][contains(text(),'Команда профессионалов')]")
        print ("Click: Начать работу")
        driver.find_element_by_xpath("//a[@class='v-btn v-btn--contained v-btn--router theme--light v-size--default']").click()
        driver.find_element_by_xpath("//div[@class='v-input pt-5 theme--light v-text-field v-text-field--is-booted v-text-field--enclosed v-text-field--outlined']//input") #
        driver.back()
        time.sleep(0.2)
        print ("Click: Как это работает")
        driver.find_element_by_xpath("//a[@class='how-btn ml-3 v-btn v-btn--contained v-btn--router theme--light v-size--default secondary']").click() # myDynamicElement = 
        driver.find_element_by_xpath("//h1[@class='display-2 text-xs-center'][contains(text(),'Как это работает')]") #
        driver.back()
        time.sleep(0.2)
        print ("Check: Блок ниже как это работает")
        driver.find_element_by_xpath("//div[@class='advantages']//div[@class='container']") #
        print ("Chekc: Блок Мы можем решить ...")
        driver.find_element_by_xpath("//div[@class='about-spec']//div[@class='container']")
        print ("Click: Все услуги")
        driver.find_element_by_xpath("//a[@class='text-xs-left v-btn v-btn--contained v-btn--router theme--light v-size--default white']").click()
        print ("Check: Страница Услуги")
        driver.find_element_by_xpath("//h1[@class='display-2'][contains(text(),'Мы работаем')]") #
        driver.back()
        time.sleep(0.2)
        print ("Check: Тарифы")
        driver.find_element_by_xpath("//h3[@class='text-xs-center display-2'][contains(text(),'Тарифы')]")
        print ("Check: Подсветка тарифы")
        elem = driver.find_elements_by_xpath("//div[@class='flex pa-3 taxes-block xs12 sm6 md3']")
        if len(elem) > 3:
            print("Кол-во неподсвеченных тарифов больше 3 падаем")
            assert False
        driver.find_elements_by_xpath("//div[@class='flex pa-3 taxes-block xs12 sm6 md3 active']")
        print ("Check: Тариф - выбрать")
        i = 0
        while i < 4:
            driver.implicitly_wait(10)
            elem = driver.find_elements_by_xpath("//div[@class='layout wrap justify-center']//a[@href='/sign_in']")
            print ("Выбрать - " + str(i))
            elem[i].click()
            driver.find_element_by_xpath("//h1[@class='display-1 mx-auto'][contains(text(),'Вход')]")
            driver.back()
            time.sleep(0.2)
            i += 1
            
        print ("Click: Наши контакты")
        driver.find_element_by_xpath("//a[@class='v-btn v-btn--contained v-btn--router theme--light v-size--default secondary']").click()
        driver.find_element_by_xpath("//h1[@class='display-2 pb-4'][contains(text(),'Свяжитесь')]")
        driver.back()
        time.sleep(0.2)
        print ("Check: Карточка служба поддержки пользователей")
        driver.find_element_by_xpath("//div[@class='flex card pa-4']")
        driver.find_element_by_xpath("//a[@class='color-blue'][contains(text(),'воспользуйтесь')]").click()
        print ("Click: Наши контакты")
        driver.find_element_by_xpath("//h1[@class='display-2 pb-4'][contains(text(),'Свяжитесь')]")
        driver.back()
        time.sleep(0.2)
        self.support_card(driver)
        self.reviews(driver)

    def support_card (self, driver): # Карточка Служба поддеркжи пользоватлей 
        print ("Check: Карточка служба поддержки пользователей")
        driver.find_element_by_xpath("//div[@class='flex card pa-4']")
        driver.find_element_by_xpath("//a[@class='color-blue'][contains(text(),'воспользуйтесь')]").click()
        print ("Click: Наши контакты")
        driver.find_element_by_xpath("//h1[@class='display-2 pb-4'][contains(text(),'Свяжитесь')]")
        driver.back()
        time.sleep(0.2)

    def reviews(self, driver): # Проверка отзывов (перелистывание отзывов и чеки)
    
        print ("Check: Отзывы")
        print ("Click: Вправо")
        text1 = driver.find_element_by_xpath("//h3[@class='text-title headline pb-3 mb-3']").text
        driver.find_element_by_xpath("//button[@class='btn-next v-btn v-btn--depressed v-btn--fab v-btn--flat v-btn--outlined v-btn--round v-btn--text theme--light v-size--default']").click()
        time.sleep(0.4)
        text2 = driver.find_element_by_xpath("//h3[@class='text-title headline pb-3 mb-3']").text
        if text1 == text2:
            assert False
        print ("Click: Влево")
        driver.find_element_by_xpath("//div[@class='v-window-item review v-window-item--active']//button[@class='btn-prev v-btn v-btn--depressed v-btn--fab v-btn--flat v-btn--outlined v-btn--round v-btn--text theme--light v-size--default']").click()
        time.sleep(0.4)
        text2 = driver.find_element_by_xpath("//h3[@class='text-title headline pb-3 mb-3']").text
        if text1 != text2:
            assert False   

    def main_sevices(self, driver): #Првоерка контента на странице услуг
        print ("Click: База знаний")
        driver.find_element_by_xpath("//div[@class='v-toolbar__items hidden-xs']//a[1]").click()
        print ("Info: Проперка страницы Услуг для неавторизованного пользвоателя")
        print ("Check: Блок Мы работаем со всему устройствами")
        driver.find_elements_by_xpath("//div[@class='layout text-xs-center pt-5 mt-4 pb-5 mb-2 column']")
        driver.find_elements_by_xpath("//h1[@class='display-2'][contains(text(),'Мы работаем')]")
        print ("Check: Блок Наши возможнсоти")
        driver.find_elements_by_xpath("//div[@id='about-spec']//div[@class='container']")
        driver.find_elements_by_xpath("//div[@class='flex text-xs-center xs12']//h2[@class='display-2'][contains(text(),'Наши')]")
        print ("Check: Блок Что получаете вы")
        driver.find_elements_by_xpath("//div[@class='advantages']//div[@class='container']")
        driver.find_elements_by_xpath("//h2[contains(text(),'Что получаете')]")
        self.reviews(driver)
        self.support_card(driver)
        print ("Check: Футер")
        driver.find_element_by_xpath("//div[@class='container footer-links']")
        driver.find_elements_by_xpath("//p[@class='body-2 text-xs-center'][contains(text(),'ООО')]")

    def footer_unauthorized(self, driver): # Чек ссылок в футоре странице
        url = driver.current_url
        print ("Info: Чек футера")
        print ("Click: Поиск и удаление вирусов")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Поиск и удаление')]").click()
        if str(url) != "http://front.stage.helpcubes.com/services":
            self.check_page_services(driver)
            driver.back()
            time.sleep(0.2)

        print ("Click: Восстановление данных")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Восстановление данных')]").click()
        if str(url) != "http://front.stage.helpcubes.com/services":
            self.check_page_services(driver)
            driver.back()
            time.sleep(0.2)

        print ("Click: Установка ПО")        
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Установка ПО')]").click()
        if str(url) != "http://front.stage.helpcubes.com/services":
            self.check_page_services(driver)
            driver.back()
            time.sleep(0.2)

        print ("Click: Этапы работы")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Этапы работы')]").click()
        if str(url) != "http://front.stage.helpcubes.com/how":
            self.check_page_how(driver)
            driver.back()
            time.sleep(0.2)
        
        print ("Click: Безопасные соединение")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Безопасное соединение')]").click()
        if str(url) != "http://front.stage.helpcubes.com/how":
            self.check_page_how(driver)
            driver.back()
            time.sleep(0.2)
        
        print ("Click: Базовый")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Базовый')]").click()
        if str(url) != "http://front.stage.helpcubes.com/tariffs":
            self.check_page_tarifs(driver)
            driver.back()
            time.sleep(0.2)
        
        print ("Click: Стандартный")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Стандартный')]").click()
        if str(url) != "http://front.stage.helpcubes.com/tariffs":
            self.check_page_tarifs(driver)
            driver.back()
            time.sleep(0.2)

        print ("Click: Оптимальный")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Оптимальный')]").click()
        if str(url) != "http://front.stage.helpcubes.com/tariffs":
            self.check_page_tarifs(driver)
            driver.back()
            time.sleep(0.2)

        print ("Click: Максимальный")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Максимальный')]").click()
        if str(url) != "http://front.stage.helpcubes.com/tariffs":
            self.check_page_tarifs(driver)
            driver.back()
            time.sleep(0.2)

        print ("Click: Часто задаваемые вопросы")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Часто задаваемые вопросы')]").click()
        if str(url) != "http://front.stage.helpcubes.com/help":
            self.check_page_help(driver)
            driver.back()
            time.sleep(0.2)

        print ("Click: Обратный звонок")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3 link']").click()
        if str(url) != "http://front.stage.helpcubes.com/contacts":
            driver.find_element_by_xpath("//h1[@class='display-2 pb-4'][contains(text(),'Свяжитесь')]")
            driver.back()
            time.sleep(0.2)


    def check_page_services(self, driver): # Проверка на то что открыта страница Услуги
        print ("Check: Блок Наши возможнсоти")
        #driver.implicitly_wait(0)
        driver.find_element_by_xpath("//div[@id='about-spec']//div[@class='container']")
        driver.find_element_by_xpath("//div[@class='flex text-xs-center xs12']//h2[@class='display-2'][contains(text(),'Наши')]").text
        #driver.implicitly_wait(10)
    
    def check_page_how(self, driver): # Проверка на то что открыта страница Как это работает
        print ("Check: Как это работает") 
        driver.find_element_by_xpath("//h1[@class='display-2 text-xs-center'][contains(text(),'Как это работает')]")

    def check_page_tarifs(self, driver): # Проверка на то что открыта страница Тарифы
        print ("Check: Тарифы для дома и офиса")
        driver.find_element_by_xpath("//h1[@class='display-2 text-xs-center'][contains(text(),'Тарифы для дома и офиса')]")

    def check_page_help(self, driver): # Проверка на то что открыта страница Помощь
        print ("Check: Помощь")
        driver.find_element_by_xpath("//h1[@class='display-1 help__title'][contains(text(),'Служба поддержки')]")

    def main_how_its_work(self,driver): # Проверка конентенрта на странице как это работает
        print ("Info: Проверка контента Как это работает")
        print ("Click: Как это работает")
        driver.find_element_by_xpath("//div[@class='navbar']//a[2]//span[1]").click()
        print ("Check: Как это работает")
        driver.find_elements_by_xpath("//h1[@class='display-2 text-xs-center'][contains(text(),'Как это работает')]")
        print ("Check: Что на фоне")
        driver.find_elements_by_xpath("//div[@class='first-bg']")
        print ("Check: Блок качество ПО")
        driver.find_elements_by_xpath("//div[@id='security']//div[@class='container']")
        print ("Check: Название Качество ПО")
        driver.find_elements_by_xpath("//h2[@class='display-2'][contains(text(),'Качественное ПО')]")
        print ("Check: Удобное и качесвтенное ПО")
        driver.find_element_by_xpath("//div[@class='grey-bg']//div[@class='layout column']")
        print ("Check: Название Удобное и качественное ПО")           
        driver.find_element_by_xpath("//h2[@class='display-2 text-xs-center'][contains(text(),'Удобный и понятный')]")        
        print ("Click: Зарегистрироваться")
        driver.find_element_by_xpath("//a[@class='reg-btn v-btn v-btn--contained v-btn--router theme--light v-size--default primary']").click()
        driver.back()
        time.sleep(0.2)
        self.support_card(driver)

    def main_tarifs (self, driver):

        print ("Info: првоерка контента на странице тарифов") #Проверка на контент страниц тарифов
        driver.find_element_by_xpath("//div[@class='navbar']//a[3]").click()
        self.check_page_tarifs(driver)
        print ("Check: Превый столбец")
        driver.find_element_by_xpath("//div[@class='flex pt-4 pb-4 mb-2 tarrifs-block-text xs12 md4']")
        print ("Check: Контент первого столбца")
        driver.find_element_by_xpath("//h3[@class='h7 pb-1'][contains(text(),'Стоимость тарифа')]")
        driver.find_element_by_xpath("//h3[@class='h7 pb-1'][contains(text(),'Доступ к базе знаний')]")
        driver.find_element_by_xpath("//p[@class='body-2 mb-1'][contains(text(),'Вы можете разделить ваш')]")
        print ("Check: Тарифы")
        driver.find_element_by_xpath("//h2[@class='title'][contains(text(),'Базовый')]")
        elem = driver.find_elements_by_xpath("//h5[@class='h7 pt-3 pb-5'][contains(text(),'')]")
        if len(elem) < 8:
            assert False
        elem = driver.find_elements_by_xpath("//img[@src='img/icons/accept.svg']")
        if len(elem) < 28:
            assert False
        driver.find_element_by_xpath("//h2[@class='title'][contains(text(),'Стандартный')]")
        driver.find_element_by_xpath("//h2[@class='title'][contains(text(),'Оптимальный')]")
        driver.find_element_by_xpath("//h2[@class='title'][contains(text(),'Максимальный')]")
        print ("Check: Выбрать")
        i = 0
        while i < 4:
            print ("Click: Выбрать " + str(i))
            elem = driver.find_elements_by_xpath("//button[@class='primary v-btn v-btn--contained theme--light v-size--default']")
            elem[i].click()
            i += 1
            driver.find_element_by_xpath("//h1[@class='display-1 mx-auto'][contains(text(),'Вход')]")
            driver.back()
            time.sleep(0.2)
        
        self.support_card(driver)
        print ("Check: Какие услуги включены")
        driver.find_element_by_xpath("//h2[@class='display-2'][contains(text(),'Какие услуги включены')]")
        driver.find_element_by_xpath("//h6[@class='title'][contains(text(),'Отладка сетей')]")
        print ("Click: Все услуги")
        driver.find_element_by_xpath("//a[@class='text-xs-left v-btn v-btn--contained v-btn--router theme--light v-size--default white']").click()
        self.check_page_services(driver)
        driver.back()
        time.sleep(0.2)
        print ("Check: логотип в футоре")
        driver.find_element_by_xpath("//div[@class='flex footer-bottom__logo xs12 md3']")


    def edit_user(self, driver):
        print ("Info: Измение информации о юзере")
        
        print ("Click: Изменить последнего пользователя в списке")
        elem_edit = driver.find_elements_by_xpath("//div[@class='flex user-card__head pb-2 pt-3 pb-3']//i[@class='v-icon material-icons theme--light'][contains(.,'create')]")
        elem_edit_desktop = (len(elem_edit) // 2) - 1 
        #elem_edit_mobile = (len(elem_edit) // 2) Потом для мобилок оставлю
        elem_edit[int(elem_edit_desktop)].click()
        
        print ("Fill: Заменить имя")
        self.clear_field(driver, "//input[@aria-label='Имя']")
        edit_name = names.get_first_name()
        driver.find_element_by_xpath("//input[@aria-label='Имя']").send_keys(edit_name)
        
        print ("Click: выставить другой пол")
        gender = "none"
        try: 
            driver.implicitly_wait(2)
            driver.find_element_by_xpath("//div[@class='v-radio theme--light v-item--active']//input[@value='female']")
            driver.find_element_by_xpath("//div[@class='v-input--selection-controls__ripple']").click()
            gender = "male"
            driver.implicitly_wait(10)
        except:
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("//div[@class='v-input--selection-controls__ripple']").click()
            gender = "female"
        
        print ("Fill: Заменить номер")
        self.clear_field(driver, "//input[@aria-label='Номер телефона']")
        driver.find_element_by_xpath("//input[@aria-label='Номер телефона']").send_keys("0987654321")
        
        print ("Fill: Заменить почту")
        mail_edit = "autotestemail"+ str(random.randint(1000000, 9999999)) + "@python.org"
        self.clear_field(driver, "//input[@aria-label='Email']")
        driver.find_element_by_xpath("//input[@aria-label='Email']").send_keys(mail_edit)

        print ("Fill: Заменить телеграм")
        self.clear_field(driver, "//input[contains(@aria-label,'Telegram')]")
        Telegram_edit = "EditHelpcubesTelegramAutotest"
        driver.find_element_by_xpath("//input[contains(@aria-label,'Telegram')]").send_keys(Telegram_edit)

        print ("Fill: Skype")
        self.clear_field(driver, "//input[contains(@aria-label,'Skype')]")
        Skype_edit = "EditHelpCubesSkypeAutotest"
        driver.find_element_by_xpath("//input[contains(@aria-label,'Skype')]").send_keys(Skype_edit)

        print ("Click: Сохранить изменения")
        driver.find_element_by_xpath("//button[@class='users-modal__button v-btn v-btn--contained theme--light v-size--default primary']").click()

        print ("Check: Имя измененное")
        driver.refresh()
        driver.find_element_by_xpath("//div[@class='flex right-block xs-8']//h3[@class='title'][contains(text(),'" + edit_name + "')]")
        print ("Check: Номер измененный")
        driver.find_element_by_xpath("//div[@class='flex right-block xs-8']//p[@class='body-1 mb-0'][contains(text(),'+7 (098) 765-43-21')]")
        print ("Check: Мэйл измененный")
        driver.find_element_by_xpath("//div[@class='flex right-block xs-8']//p[@class='body-1 mb-0'][contains(text(),'" + mail_edit + "')]")
        print ("Check: Skype изменыеннй")
        driver.find_element_by_xpath("//div[@class='flex right-block xs-8']//p[@class='body-1 mb-0'][contains(text(),'" + Skype_edit + "')]")
        print ("Check: Telegram измененный")
        driver.find_element_by_xpath("//div[@class='flex right-block xs-8']//p[@class='body-1 mb-0'][contains(text(),'" + Telegram_edit + "')]")
        
        print ("Check: Пол измененный") 

        print ("Click: Редактирование пользоваетля - посмотерть пол")
        elem_edit = driver.find_elements_by_xpath("//div[@class='flex user-card__head pb-2 pt-3 pb-3']//i[@class='v-icon material-icons theme--light'][contains(.,'create')]")
        elem_edit_desktop = (len(elem_edit) // 2) - 1 
        elem_edit[int(elem_edit_desktop)].click()
        
        if gender == "female":
            driver.find_element_by_xpath("//div[@class='v-radio theme--light v-item--active']//input[@value='female']")
        else:
            driver.find_element_by_xpath("//div[@class='v-radio theme--light v-item--active']//input[@value='male']")
        print ("Check: Пол измененный - OK")
        
        time.sleep(0.1)
        print ("Click: Отмена - выход из формы редактирования пользователя")
        driver.find_element_by_xpath("//button[@class='users-modal__button v-btn v-btn--contained theme--light v-size--default secondary']").click()

    def user_delete (self, driver):

        #self.add_user(driver) ##############################
        
        print ("Info: Нахождение всех пользователей в аккаунте")
        user_len = len(driver.find_elements_by_xpath("//div[@class='v-card__text user-card__body']")) // 2

        print ("Info: кол-во пользователей = "+ str(user_len))

        print ("Click: Удаление пользователя")
        delete_button = driver.find_elements_by_xpath("//div[@class='flex user-card__head pb-2 pt-3 pb-3']//i[@class='v-icon material-icons theme--light'][contains(.,'delete')]")
        delete_button_desktop = (len(delete_button) // 2) - 1
        #delete_button_desktop = (len(delete_button) // 2) для мобилок
        delete_button[delete_button_desktop].click()
        print ("Click: Подтвердить удаление пользователя")
        time.sleep(0.4)
        driver.find_element_by_xpath("//span[@class='v-btn__content'][contains(.,'Удалить')]").click()

        print ("Check: Пользователей стало меньше?")
        driver.refresh()
        user_len_after = len(driver.find_elements_by_xpath("//div[@class='v-card__text user-card__body']")) // 2
        if int(user_len) - 1 == int(user_len_after):
            print ("Info: пользователь успешно удален")
        else: 
            print ("Info: пользователей не соотвествует ожидаемому кол-ву")
            assert False

    def device_edit(self, driver):
        print ("Info: Изменение информации о устройстве")

        print ("Click: Устрйоство: Отредактировать последнее")
        device_edit_button = driver.find_elements_by_xpath("//div[@class='flex device-card__head pb-2 pt-3 pb-3']//i[@class='v-icon material-icons theme--light'][contains(.,'create')]")
        device_edit_button_desktop = ( len(device_edit_button) // 2 ) - 1
        device_edit_button[device_edit_button_desktop].click()

        print ("Fill: Устройство: Изменить название ")
        self.clear_field(driver, "//input[@aria-label='Название']")
        device_name = names.get_full_name()
        driver.find_element_by_xpath("//input[@aria-label='Название']").send_keys(device_name)

        print ("Fill: Устройство: Изменить производителя")
        self.clear_field(driver, "//input[contains(@aria-label,'Производитель')]")
        driver.find_element_by_xpath("//input[contains(@aria-label,'Производитель')]").send_keys(device_name)

        print ("Fill: Устроство: Изменит модель")
        self.clear_field(driver, "//input[contains(@aria-label,'Производитель')]")
        driver.find_element_by_xpath("//input[contains(@aria-label,'Производитель')]").send_keys(device_name)

        print ("Fill: Устройство: Изменить тип")
        driver.find_element_by_xpath("//div[@class='flex pr-3 pa-md-0 xs12 md6']//div[@class='device-modal__field']//i[@class='v-icon mdi mdi-menu-down theme--light']").click()
        time.sleep(0.1)
        driver.find_element_by_xpath("//div[@class='v-list-item__title'][contains(.,'Планшет')]").click()
        
        print ("Fill: Устройство: Операционная систем")
        driver.find_element_by_xpath("//div[@class='flex pl-3 pa-md-0 xs12 md6']//i[@class='v-icon mdi mdi-menu-down theme--light']").click()
        time.sleep(0.1)
        driver.find_element_by_xpath("//div[contains(text(),'Windows 7')]").click()

        print ("Click: Сохранить изменения")
        driver.find_element_by_xpath("//button[@class='device-modal__button v-btn v-btn--contained theme--light v-size--default primary']").click()

        print ("Info: Устройство: Проверка измененной инфомрации")
        
        print ("Check: Устройство: Название")
        driver.find_element_by_xpath("//div[@class='flex right-block xs-8']//h3[@class='title'][contains(text(),'"+ device_name + "')]")

        print ("Check: Устройство: Тип устрйоства")
        driver.find_element_by_xpath("//div[@class='v-card__text device-card__body']//p[@class='body-1 mb-0'][contains(text(),'Планшет')]")

        print ("Check: Устройство: Операционная систем")
        driver.find_element_by_xpath("//div[@class='v-card__text device-card__body']//p[@class='body-1 mb-0'][contains(text(),'Windows 7')]")

        print ("Check: Устройство: Производитель")
        driver.find_element_by_xpath("//div[@class='flex right-block xs-8']//p[@class='body-1 mb-0'][contains(text(),'" + device_name + "')]")

    def device_delete(self, driver):
        
        print ("Info: Устройство: Удаление")

        print ("Check: Устройства: найти все доступные устрйоства")
        device_count = driver.find_elements_by_xpath("//div[@class='v-card__text device-card__body']")

        time.sleep(0.2)
        print ("Click: Устройство: Удалить последнее")
        button_delete = driver.find_elements_by_xpath("//div[@class='device-card v-card v-sheet v-sheet--tile theme--light']//i[@class='v-icon material-icons theme--light'][contains(text(),'delete')]")
        button_delete_desktop = (len(button_delete) // 2) - 1 
        button_delete[button_delete_desktop].click()

        print ("Click: Подтвердить удаление")
        driver.find_element_by_xpath("//div[@class='v-dialog confirm-modal v-dialog--active v-dialog--persistent']//button[@class='v-btn v-btn--contained theme--light v-size--default red-gradient']").click()

        print ("Check: Устройтсво: Проверка отсутвия лишенго компонента")
        driver.refresh()
        device_count_after = driver.find_elements_by_xpath("//div[@class='v-card__text device-card__body']")
        if len(device_count) - 2 == len(device_count_after):
            print ("Check: Устройтсво: Проверка отсутвия лишенго компонента - ОК")
        else:
            print ("Check: Устройство: неверное кол-во устройств - ERROR")
            assert False

    def change_password(self, driver): # изменяет пароль затем отправляет запрос на его обратное восстановление, чтоб не было костылей.
        print ("Info: Смена пароля пользователя")

        self.wait_loss(driver, "//div[@class='nuxt-progress']")

        print ("Click: Сменить пароль")
        driver.find_element_by_xpath("//button[@type='button'][contains(.,'Сменить пароль')]").click()

        print ("Fill: Ввести пароль")
        driver.find_element_by_xpath("//input[contains(@placeholder,'Текущий пароль')]").send_keys("23072307")

        print ("Fill: Сменить пароль - основное")
        driver.find_element_by_xpath("//input[@placeholder='Введите новый пароль']").send_keys("23072307qS")

        print ("Fill: Сменить пароль - повторить")
        driver.find_element_by_xpath("//input[@placeholder='Подтвердите новый пароль']").send_keys("23072307qS")

        print ("Click: Сменить пароль")
        driver.find_element_by_xpath("//span[@class='v-btn__content'][contains(.,'Сменить пароль')]").click()

        time.sleep(0.5) #Слишком быстро отправляется запрос
        print ("Fill: Вернуть пароль обратно")
        test_request = request_hc()
        test_request.get_back_passwrod(self.site(), self.get_email_from_config(), "23072307qS")


    def support_page_send_(driver):

        print ("Проверка элементов на странице /support")
        

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import names
import pyperclip
import configparser
import getpass
from browsers import browsers
from colorama import Fore, Style
from selenium.webdriver.common.action_chains import ActionChains

# Print status
# Click
# Check
# Info
# Fill
#        print ("Click: Бургер")
# i = 0 
# while i < 100:
#               d
#       i = 200
# except:
# i += 1
# time.sleep(0.1)river.
# find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
#

class hc_command_mobile():

    mail = "qwe"

    def click_burger(self, driver):
        print ("Click: Бургер")
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
                i = 200
            except:
                i += 1
                time.sleep(0.1)

  
    def try_click_fast(self, driver, element):
        i = 0 
        while i < 100:
            try:
                driver.implicitly_wait(0.1)
                driver.find_element_by_xpath(element).click()
                i = 100
            except:
                i += 1
                if i == 99:
                    print ("Info: Не удалось нажать элемент: " + element)
                    assert False
                time.sleep(0.1)
        driver.implicitly_wait(10)

    def signin(self, driver): #логиниться на helpcubes
        #Войти в аккаунт
        print ("Click: Бургер")
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
                i = 200
            except:
                i += 1
                time.sleep(0.1)
        print ("Click: Вход в аккаунт")
        driver.find_element_by_xpath("//a[@class='mt-4 v-btn v-btn--depressed v-btn--flat v-btn--outlined v-btn--router theme--light v-size--default primary--text']").click()

        #Заполнение формы ввода
        mail = self.__memory_mail()
        print("Fill: форма входа пользвоаель")
        driver.find_element_by_xpath("(//div[@class='v-input pt-5 theme--light v-text-field v-text-field--is-booted v-text-field--enclosed v-text-field--outlined']//input)").send_keys(mail)
        driver.find_element_by_xpath("(//input[@name='password'])").send_keys("23072307")

        #Войти
        print ("Click: Войти")
        driver.find_element_by_xpath("(//button[@class='v-btn v-btn--contained theme--light v-size--default'])").click()

        #Скипнуть момент добавления карты - Открывается главная страница
        print ("Скипнуть момент добавления карты - Открывается главная страница")
        try:
            driver.find_element_by_xpath("//button[@class='v-btn v-btn--depressed v-btn--flat v-btn--outlined theme--light v-size--default primary--text']").click()
        except:
            print("фывалдо")

    def setting(self, driver): #заходит в настройки пользователя
        print ("Click: Бургер")
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
                i = 200
            except:
                i += 1
                time.sleep(0.1)
        print("Click: Настройки пользваоеля")
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//a[@class='profile__settings']//span").click()
                i = 200
            except Exception as e:
                print (e)
                i += 1
                time.sleep(0.1)

    def setting_devices(self, driver): #открыть пользователи и устройства
        print ("Click: Открыть пользователи и устройства")
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        driver.find_element_by_xpath("//div[@class='lk-menu-mob visible-xs']//a[2]").click()

    def add_devices(self, driver): #добавление устройства
        print ("Info: Добавление устройство для пользователя")
        print ("Click: Добавить устройствво")
        driver.find_element_by_xpath("//div[@class='container bg-white']//div[@class='flex pt-4 mt-2']//span[@class='v-btn__content']").click()    

        print ("Fill: Название устройства")
        name = names.get_full_name()
        elem = driver.find_elements_by_xpath("//div[@class='v-text-field__slot']//input")
        elem_click = elem[0]
        elem_click.send_keys(name)

        print ("Fill: Производитель")
        elem_click = elem[1]
        elem_click.send_keys(name)

        print ("Fill: Модель")
        elem_click = elem[2]
        elem_click.send_keys("autotest")

        # выбор типа устройства
        print ("Select: Тип устройства")
        elem = driver.find_elements_by_xpath("//div[@class = 'v-select__selections']")
        elem_click = elem[0]
        elem_click.click()

        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//div[@class='v-menu__content theme--light v-menu__content--fixed menuable__content__active']//div[@class='v-list v-sheet v-sheet--tile theme--light']//div[1]//div[1]//div[1]").click()
                i = 200
            except Exception as e:
                print (e)
                i += 1
                time.sleep(0.1)


        # выбор операционной систомы
        print ("Select: ОС девайса")
        elem_click = elem[1]
        elem_click.click()
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
        driver.find_element_by_xpath("//button[@class='device-modal__button v-btn v-btn--contained theme--light v-size--default primary']").click()
        
        print("Site refresh")
        driver.refresh()
        
        # проверка данных
        print ("Info: Проверка добавленного устройств")
        print ("Check: Название деваса")
        driver.find_element_by_xpath("//div[@class='flex xs8']//h3[@class='title'][contains(text(),'" + name + "')]")
        print ("Check: Тип девайса")
        driver.find_elements_by_xpath("//p[@class='body-1 mb-0'][contains(text(),'Настольный компьютер')]")
        print ("Check: ОС девайсас")
        driver.find_elements_by_xpath("//p[@class='body-1 mb-0'][contains(text(),'Windows 10')]")
        print ("Check: Производитель девайса")
        driver.find_elements_by_xpath("//p[@class='body-1 mb-0'][contains(text(),'" + name + "')]")
        print ("Check: Модель девайса")
        driver.find_elements_by_xpath("//p[@class='body-1 mb-0'][contains(text(),'autotest')]")
        
        print ("Info: Устройство добавлено. Данные проверены после перезагрузки")

    def support_message(self,driver): #Заполениен формы отправки сообщения в службу поддержки
        
        print ("Info: Заполнение и отправки формы в ТП")
        #Написать в поддержку
        print ("Click: Открытие формы отправки сообщения в ТП")
        driver.find_element_by_xpath("//div[@class='text-xs-right my-auto']//button[@type='button']").click()

        print ("Fill: Тема обращения")
        #Заполенние формы поддержки
        summary = "AUTOTEST messege in support"
        driver.find_element_by_xpath("//input[@name='name']").send_keys(summary)
        
        #Выбор категории устройства
        elem_list = driver.find_elements_by_xpath("//div[@class='v-select__selections']")
        print ("Select: Категория обращения")
        elem = elem_list[0]
        elem.click() 
        time.sleep(1)
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/div[@class='v-menu__content theme--light v-menu__content--fixed menuable__content__active']/div[@class='v-select-list v-card theme--light']/div[@class='v-list v-sheet v-sheet--tile theme--light']/div[1]/div[1]").click()
                i = 200
            except:
                i += 1
                time.sleep(0.1)
        
        #Выбор устройства из списка
        print ("Select: Устрйоство")
        elem = elem_list[1]
        elem.click()

        driver.find_element_by_xpath("//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/div[@class='v-menu__content theme--light v-menu__content--fixed menuable__content__active']/div[@class='v-select-list v-card theme--light']/div[@class='v-list v-sheet v-sheet--tile theme--light']/div[2]/div[1]").click()
        
        #Выбор пользователя из списка
        print ("Select: Пользователь")
        elem = elem_list[2]
        elem.click()
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/div[@class='v-menu__content theme--light v-menu__content--fixed menuable__content__active']/div[@class='v-select-list v-card theme--light']/div[@class='v-list v-sheet v-sheet--tile theme--light']/div[2]/div[1]").click()
                i = 200
            except:
                i += 1
                time.sleep(0.1)
        
        #Добавление комментария
        print ("Fill: Описание проблемы")
        description = "Lorem ipsum dolor sit amet"
        driver.find_element_by_xpath("//textarea[@name='comment']").send_keys("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.")
        
        #Добавление файла
        print ("Fill: Добавление файла")
        driver.find_element_by_xpath("//input[@name='files[]']").send_keys("C:\\Users\\" + getpass.getuser()  + "\\Documents\\GitHub\\HC_autotest\\ford-ford-raptor-parketnik-dzhip.jpeg")
        
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
        print ("Click: Бургер")
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
                i = 200
            except:
                i += 1
                time.sleep(0.1)
        print ("Click: Регистрация")
        #Неавторизованный пользовать - Регистрация
        driver.find_element_by_xpath("//a[@class='mt-2 v-btn v-btn--contained v-btn--router theme--light v-size--default primary']").click()

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
        driver.find_element_by_xpath("(//button[@class='v-btn v-btn--contained theme--light v-size--default'])").click()

        #выход на главную
        driver.find_element_by_xpath("//button[@class='v-btn v-btn--contained theme--light v-size--default primary']").click()

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
        print ("Info: Добавления тариф для пользователя")
        print ("Click: Бургер")
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
                i = 200
            except:
                i += 1
                time.sleep(0.1)
        #Раздел: Тарифы
        print ("Click: Тарифы")
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//p//a[@href='/tariffs']").click()
                i = 200
            except Exception as e:
                print (e)
                i += 1
                time.sleep(0.1)


        #Выбрать второй тариф максимальный
        print ("Click: Выбрать тариф")
        elem_list = driver.find_elements_by_xpath("//button[@class='primary v-btn v-btn--contained theme--light v-size--default']")
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
        print ("Click: Бургер")
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
                i = 200
            except:
                i += 1
                time.sleep(0.1)
        #Войти в аккаунт
        print ("Click: Вход в аккаунт")
        driver.find_element_by_xpath("(//a[@class='mt-4 v-btn v-btn--depressed v-btn--flat v-btn--outlined v-btn--router theme--light v-size--default primary--text'])").click()

        #Заполнение формы ввода
        print ("Fill: mail")
        driver.find_element_by_xpath("(//div[@class='v-input pt-5 theme--light v-text-field v-text-field--is-booted v-text-field--enclosed v-text-field--outlined']//input)").send_keys(login)
        print ("Fill: pass")
        driver.find_element_by_xpath("(//input[@name='password'])").send_keys(password)

        #Войти
        print ("Click: Вход после заполения полей")
        driver.find_element_by_xpath("(//button[@class='v-btn v-btn--contained theme--light v-size--default'])").click()

        #Скипнуть момент добавления карты - Открывается главная страница
        try:
            driver.implicitly_wait(2)
            driver.find_element_by_xpath("//button[@class='v-btn v-btn--depressed v-btn--flat v-btn--outlined theme--light v-size--default primary--text']").click()
            driver.implicitly_wait(10)
        except:
            print("фывалдо")
            driver.implicitly_wait(10)


    def add_profile_info(self, driver): #Заполнение информации о пользваотеле
        print ("Info: заполнение основной информации о пользователе")
        # Добавление фотки
        print ("Fill: Добавление фотки")
        driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\" + getpass.getuser()  + "\\Documents\\GitHub\\HC_autotest\\ford-ford-raptor-parketnik-dzhip.jpeg")
        # Изменение фамилии
        print ("Fill: Добавление фамилии")
        last_name = names.get_last_name()
        driver.find_element_by_xpath("//input[@name='last_name']").send_keys(last_name)
        # Вставка дату рождения
        print ("Fill: Заполнение даты рождения")
        dateofbirth = "14.04.1986"
        driver.find_element_by_xpath("//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/div[@class='application--wrap']/main[@class='v-content']/div[@class='v-content__wrap']/div[@class='account-bg']/div[@class='container pa-xs-0']/div[@class='layout column']/div[@class='flex right-block xs12 md8']/div[@class='bg-xs-white']/form[@id='form']/div[@class='mx-auto v-card v-sheet v-sheet--tile theme--light']/div[@class='v-card__text pt-xs-0 px-xs-4']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys(dateofbirth)
        # Женский пол
        print ("Click: Установить женский пол")
        elem = driver.find_elements_by_xpath("//div[@class='v-input--selection-controls__ripple']")
        elem_click = elem[1]
        elem_click.click()
        time.sleep(0.5)
        # Изменение номера телефона
        print ("Fill: Установить номер телефона")
        driver.find_element_by_xpath("//input[@placeholder='+7 (###) ###-##-##']").send_keys("1234567890")     
        # Сохранить изменения
        time.sleep(0.5)
        print ("Click: Сохранить")
        driver.find_element_by_xpath("//button[@class='v-btn v-btn--block v-btn--contained theme--light v-size--default primary']").click()
        time.sleep(0.5)
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
        driver.find_element_by_xpath("//div[@class='container bg-white']//div[@class='flex pt-4 mt-2 pb-2']//button[@class='v-btn v-btn--contained theme--light v-size--default secondary']").click()

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
        driver.find_element_by_xpath("//div[@class='user-card v-card v-sheet v-sheet--tile theme--light']//h3[@class='title'][contains(text(),'" + name + "')]")
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
        print ("Click: Бургер")
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
                i = 200
            except:
                i += 1
                time.sleep(0.1)
        # Открыть контакты
        print ("Click: Открыть страницу Контакты")
        driver.find_element_by_xpath("//p[@class='header__link']//a[@href='/contacts']").click()

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

        # Вход в аккаунт
        print ("Fill: Логин Jira")
        driver.find_element_by_xpath("//input[@id='login-form-username']").send_keys("vermowl")
        print ("Fill: Пароль Jira")
        driver.find_element_by_xpath("//input[@id='login-form-password']").send_keys("9575344GHty")
        print ("Click: Логин")
        driver.find_element_by_xpath("//input[@id='login-form-submit']").click()
        driver.implicitly_wait(10)

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
        #Войти в аккаунт
        print ("Info: Открыть форму входа")
        print ("Click: Бургер")
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
                i = 200
            except:
                i += 1
                time.sleep(0.1)
        print ("Click: Вход в аккаунт")
        driver.find_element_by_xpath("//a[@class='mt-4 v-btn v-btn--depressed v-btn--flat v-btn--outlined v-btn--router theme--light v-size--default primary--text']").click()


    def open_registration_form(self,driver): #Окткрыть форму регистрациии пользвоателя
        time.sleep(1)
        print ("Info: Открыть форму регистрации польвателя")
        print ("Click: Регистрация")
        driver.find_element_by_xpath("//span[@class='v-btn__content'][contains(text(),'Регистрация')]").click()
        time.sleep(1)

    def open_user_agreement(self, driver): #Открыть страницу пользвоательского соглашения
        print ("Info: Открыть страницу пользвоательского соглашения")
        window_before = driver.window_handles[0]
        print ("Click: Политика конфиденциальности")
        driver.find_element_by_xpath("//a[@target='_blank'][contains(text(),'Политика конфиденциальности')]").click()
        time.sleep(0.1)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        self.check_user_agreement(driver)
        driver.switch_to_window(window_before)

    def check_user_agreement(self, driver): #Проверить контент страницы пользовательского соглашения
        print ("Check: Пользвоательское соглашение проверены")
        driver.find_elements_by_xpath("//li[contains(text(),'Предоставляя услуги сайта Администрация,')]")
        
        
    def open_privacy_policy(self, driver): #Открыть форму политики кионфиденкиальности
        print ("Info: Октрыть страницу политики конфиденциальности пользователя")
        window_before = driver.window_handles[0]
        print ("Click: Пользовательское соглашение")
        driver.find_element_by_xpath("//a[@target='_blank'][contains(text(),'Пользовательское соглашение')]").click()
        time.sleep(0.1)
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
        elem_click = elem[0]
        elem_click.click()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        print ("Info: Берем 4 тему")
        elem = driver.find_elements_by_xpath("//div[@class='pop-card-mob__head']")
        elem_click = elem[3]
        theme = elem_click.text
        
        def __search_check(theme, driver):
            print ("Fill: Поле поиска: Поиск по ранее найденной 4 теме")
            driver.find_element_by_xpath("//input[@placeholder='Что вы хотите узнать?']").send_keys(theme)
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
        print ("Click: Бургер")
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
                self.wait_loss(driver, "//div[@class='nuxt-progress']")
                i = 200
            except:
                i += 1
                time.sleep(0.1)
        time.sleep(1)
        print ("Click: База знаний")
        driver.find_element_by_xpath("//p[@class='header__link']//a[@class='nuxt-link-active']").click()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")

        __search_check(theme, driver)
        print ("Click: Бургер")
        i = 0 
        while i < 100:
            try:
                driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
                self.wait_loss(driver, "//div[@class='nuxt-progress']")
                i = 200
            except:
                i += 1
                time.sleep(0.1)
        
        print ("Click: База знаний")
        driver.find_element_by_xpath("//p[@class='header__link']//a[@class='nuxt-link-active']").click()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        
    def tag_filter(self,driver): #Проверка работы плиток и нахождение тэгов в Базе знаний
        print ("Info: Проверка тэгов (Плитка)")
        print ("Check: Нахождение всех плиток")
        test_item = driver.find_elements_by_xpath("//div[@class='tag-items__item']")
        j = 0
        for elem_click in test_item:
            test_item = driver.find_elements_by_xpath("//div[@class='tag-items__item']")
            tile = test_item[j].text

            print ("Click: Плитка - " +  tile)
            test_item[j].click()
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
            print ("Click: Бургер")
            i = 0 
            while i < 100:
                try:
                    driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
                    i = 200
                except:
                    i += 1
                    time.sleep(0.1)
            self.wait_loss(driver, "//div[@class='nuxt-progress']")
            print ("Click: База знаний")
            driver.find_element_by_xpath("//p[@class='header__link']//a[@class='nuxt-link-active']").click()
            self.wait_loss(driver, "//div[@class='nuxt-progress']")
            j += 1

    def popular_article(self, driver): # Проверка популярных записей в Базе знаний
        print ("Info: Проверка популярных сайтов")
        print ("Check: Популярные записи")
        driver.find_element_by_xpath("//div[@class='v-tab v-tab--active']")
        print ("Check: 5 элементов в разделе Популярные записи")
        size = len(driver.find_elements_by_xpath("//div[@class='pop-card-mob visible-xs-only']"))
        if size != 5:
            print (Fore.RED + "Info: Кол-во записей не равное 5 в разделе Популярные записи - Падаем" + Style.RESET_ALL)
            assert False
        print ("Click: Последнее")
        driver.find_element_by_xpath("//div[@class='v-tab']").click() 
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        print ("Check: 5 элментов в разделе Последние добавленные записи")
        size = len(driver.find_elements_by_xpath("//div[@class='pop-card-mob visible-xs-only']"))
        if size != 10:
            print (Fore.RED + "Info: Кол-во записей не равное 5 в разделе Популярные записи - Падаем" + Style.RESET_ALL)
            assert False
        

        
    def change_rating (self,driver): #Проверка возможности поставить голоса за или против
        driver.refresh()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        print ("Info: Добавить рейтинг статье") #
        ratings = driver.find_elements_by_xpath("//p[@class='body-1 mb-0 py-1 text-xs-center']")
        rating = ratings[0].text
        rating_int = int(rating) + 1 
        print ("Click: Лайкнуть статью")
        up_rating_buttons = driver.find_elements_by_xpath("//button[@class='btn-prev v-btn v-btn--depressed v-btn--fab v-btn--flat v-btn--outlined v-btn--round v-btn--text theme--light v-size--default']")
        up_rating_buttons[0].click()
        driver.refresh()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        check_rating = driver.find_elements_by_xpath("//p[@class='body-1 mb-0 py-1 text-xs-center']")
        print ("Check: У статьи выше рейтинг?")
        if str(check_rating[0].text) == str(rating_int):
            print ("Info: Кол-во голосов неверное - падаме")
            assert False
        print ("Chekc: Изменения цвета кнопки изменения рейтинга")
        print ("Info: Отнять рейтинг у статьи") #
        ratings = driver.find_elements_by_xpath("//p[@class='body-1 mb-0 py-1 text-xs-center']")
        rating = ratings[2].text
        rating_int = int(rating) - 1 
        print ("Click: Лайкнуть статью")
        up_rating_buttons = driver.find_elements_by_xpath("//button[@class='btn-next v-btn v-btn--depressed v-btn--fab v-btn--flat v-btn--outlined v-btn--round v-btn--text theme--light v-size--default']")
        up_rating_buttons[2].click()
        driver.refresh()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        check_rating = driver.find_elements_by_xpath("//p[@class='body-1 mb-0 py-1 text-xs-center']")
        print ("Check: У статьи выше рейтинг?")
        if str(check_rating[2].text) == str(rating_int):
            print ("Info: Кол-во голосов неверное - падаме")
            assert False
        print ("Chekc: Изменения цвета кнопки изменения рейтинга")

    def chips_and_link_test (self, driver):
        print ("Info: Проверка Chips и линки Показать все")
        print ("Click: По чипсе")
        chips = driver.find_elements_by_xpath("//span[@class='caption chips']")
        chips_text = chips[0].text
        chips[0].click()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        print ("Check: Активный элемент в самом низу " + str(chips_text))
        check = driver.find_element_by_xpath("//div[@class='v-list-item v-list-item--link theme--light active-item']").text
        if check in chips_text:
            print ("Info: Название не подсвечено справа - падаем")
            print (check)
            print (chips_text)
            assert False
        driver.back()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        print ("Click: По Показать все")
        driver.find_element_by_xpath("//a[@class='view-all']").click()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        print ("Check: Активный элемент справой стороны Все статьи")
        check = driver.find_element_by_xpath("//div[@class='v-list-item v-list-item--link theme--light active-item']").text
        if check in "Все статьи":
            print ("Info: Название не подсвечено справа - падаем")
            print (check)
            print (chips_text)
            assert False

        driver.back()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")

    def copy_link_to_article (self, driver): #Првоеряет работу линков с чипсы Поделиться
        print ("Info: Проверка работы Копирвоание ссылки для статьи в Базе щнаний")
        title_before = driver.find_elements_by_xpath("//a[@class='pop-card-mob__title']")[0].text
        print ("Click: Поделиться ссылкой")
        driver.find_elements_by_xpath("//button[@class='pop-btn v-btn v-btn--contained theme--dark v-size--default']")[0].click()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        
        print ("Click: Копировать ссылку")
        driver.find_element_by_xpath("//div[@class='pop__copy v-list-item theme--light']//a").click()
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        print ("Переход по ссылке")
        driver.get(pyperclip.paste())
        self.wait_loss(driver, "//div[@class='nuxt-progress']")
        print ("Check: Правильная открылась статья?")
        title_after = driver.find_element_by_xpath("//h1[@class='card-full__title display-1']").text
        if title_after != title_before:
            print("Info: Статьи не совпали - падаем")
            assert False
        driver.back()        
        self.wait_loss(driver, "//div[@class='nuxt-progress']")


    def wait_loss(self, driver, what_wait):
        result = False
        driver.implicitly_wait(1)
        try: 
            driver.find_element_by_xpath(what_wait)
            result = False
        except:
            result = True
        if result != True:
            self.wait_loss(driver, what_wait)        
        driver.implicitly_wait(10)    

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
        print ("Click: Как это работает")
        driver.find_element_by_xpath("//a[@class='how-btn ml-3 v-btn v-btn--contained v-btn--router theme--light v-size--default secondary']").click() # myDynamicElement = 
        driver.find_element_by_xpath("//h1[@class='display-2 text-xs-center'][contains(text(),'Как это работает')]") #
        driver.back()
        print ("Check: Блок ниже как это работает")
        driver.find_element_by_xpath("//div[@class='advantages']//div[@class='container']") #
        print ("Chekc: Блок Мы можем решить ...")
        driver.find_element_by_xpath("//div[@class='about-spec']//div[@class='container']")
        print ("Click: Все услуги")
        driver.find_element_by_xpath("//a[@class='text-xs-left v-btn v-btn--contained v-btn--router theme--light v-size--default white']").click()
        print ("Check: Страница Услуги")
        driver.find_element_by_xpath("//h1[@class='display-2'][contains(text(),'Мы работаем')]") #
        driver.back()
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
            i += 1
            
        print ("Click: Наши контакты")
        driver.find_element_by_xpath("//a[@class='v-btn v-btn--contained v-btn--router theme--light v-size--default secondary']").click()
        driver.find_element_by_xpath("//h1[@class='display-2 pb-4'][contains(text(),'Свяжитесь')]")
        driver.back()
        print ("Check: Карточка служба поддержки пользователей")
        driver.find_element_by_xpath("//div[@class='flex card pa-4']")
        driver.find_element_by_xpath("//a[@class='color-blue'][contains(text(),'воспользуйтесь')]").click()
        print ("Click: Наши контакты")
        driver.find_element_by_xpath("//h1[@class='display-2 pb-4'][contains(text(),'Свяжитесь')]")
        driver.back()
        self.support_card(driver)
        self.reviews(driver)

    def support_card (self, driver): # Карточка Служба поддеркжи пользоватлей 
        print ("Check: Карточка служба поддержки пользователей")
        driver.find_element_by_xpath("//div[@class='flex card pa-4']")
        driver.find_element_by_xpath("//a[@class='color-blue'][contains(text(),'воспользуйтесь')]").click()
        print ("Click: Наши контакты")
        driver.find_element_by_xpath("//h1[@class='display-2 pb-4'][contains(text(),'Свяжитесь')]")
        driver.back()

    def reviews(self, driver): # Проверка отзывов (перелистывание отзывов и чеки)
    
        print ("Check: Отзывы")
        print ("Click: Вправо")
        text1 = driver.find_element_by_xpath("//h3[@class='text-title headline pb-3 mb-3']").text
        driver.find_element_by_xpath("//button[@class='reviews__mobile-button btn-next v-btn v-btn--depressed v-btn--fab v-btn--flat v-btn--outlined v-btn--round v-btn--text theme--light v-size--default']").click()
        time.sleep(0.4)
        text2 = driver.find_element_by_xpath("//h3[@class='text-title headline pb-3 mb-3']").text
        if text1 == text2:
            assert False
        print ("Click: Влево")
        driver.find_element_by_xpath("//button[@class='reviews__mobile-button btn-prev v-btn v-btn--depressed v-btn--fab v-btn--flat v-btn--outlined v-btn--round v-btn--text theme--light v-size--default']").click()
        time.sleep(0.4)
        text2 = driver.find_element_by_xpath("//h3[@class='text-title headline pb-3 mb-3']").text
        if text1 != text2:
            assert False   

    def main_sevices(self, driver): #Првоерка контента на странице услуг
        
        print ("Info: Проперка страницы Услуг для неавторизованного пользвоателя")
        self.click_burger(driver)
        print ("Click: Услуги")
        driver.find_element_by_xpath("(//a[@href='/services'])[1]").click()
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

        print ("Click: Восстановление данных")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Восстановление данных')]").click()
        if str(url) != "http://front.stage.helpcubes.com/services":
            self.check_page_services(driver)
            driver.back()

        print ("Click: Установка ПО")        
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Установка ПО')]").click()
        if str(url) != "http://front.stage.helpcubes.com/services":
            self.check_page_services(driver)
            driver.back()

        print ("Click: Этапы работы")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Этапы работы')]").click()
        if str(url) != "http://front.stage.helpcubes.com/how":
            self.check_page_how(driver)
            driver.back()
        
        print ("Click: Безопасные соединение")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Безопасное соединение')]").click()
        if str(url) != "http://front.stage.helpcubes.com/how":
            self.check_page_how(driver)
            driver.back()
        
        print ("Click: Базовый")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Базовый')]").click()
        if str(url) != "http://front.stage.helpcubes.com/tariffs":
            self.check_page_tarifs(driver)
            driver.back()
        
        print ("Click: Стандартный")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Стандартный')]").click()
        if str(url) != "http://front.stage.helpcubes.com/tariffs":
            self.check_page_tarifs(driver)
            driver.back()

        print ("Click: Оптимальный")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Оптимальный')]").click()
        if str(url) != "http://front.stage.helpcubes.com/tariffs":
            self.check_page_tarifs(driver)
            driver.back()

        print ("Click: Максимальный")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Максимальный')]").click()
        if str(url) != "http://front.stage.helpcubes.com/tariffs":
            self.check_page_tarifs(driver)
            driver.back()

        print ("Click: Часто задаваемые вопросы")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3'][contains(text(),'Часто задаваемые вопросы')]").click()
        if str(url) != "http://front.stage.helpcubes.com/help":
            self.check_page_help(driver)
            driver.back()

        print ("Click: Обратный звонок")
        driver.find_element_by_xpath("//a[@class='body-2 mb-3 link']").click()
        if str(url) != "http://front.stage.helpcubes.com/contacts":
            driver.find_element_by_xpath("//h1[@class='display-2 pb-4'][contains(text(),'Свяжитесь')]")
            driver.back()


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
        self.click_burger(driver)
        print ("Click: Как это работает")
        driver.find_element_by_xpath("(//a[@href='/how'][contains(.,'Как это работает')])[1]").click()
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
        self.support_card(driver)

    def main_tarifs (self, driver):

        print ("Info: првоерка контента на странице тарифов") #Проверка на контент страниц тарифов
        self.click_burger(driver)
        driver.find_element_by_xpath("(//a[@href='/tariffs'][contains(.,'Тарифы')])[1]").click()
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
            elem = driver.find_elements_by_xpath("//button[@class='v-btn v-btn--contained theme--light v-size--default primary']")
            elem[i].click()
            i += 1
            driver.find_element_by_xpath("//h1[@class='display-1 mx-auto'][contains(text(),'Вход')]")
            driver.back()
        
        self.support_card(driver)
        print ("Check: Какие услуги включены?")
        driver.find_element_by_xpath("//h2[@class='display-2'][contains(text(),'Какие услуги включены')]")
        driver.find_element_by_xpath("//h6[@class='title'][contains(text(),'Отладка сетей')]")
        print ("Click: Все услуги")
        driver.execute_script("window.scrollTo(0, -500)") 
        self.try_click_fast(driver, "//span[@class='v-btn__content'][contains(.,'Все услуги')]")
        self.check_page_services(driver)
        driver.back()
        print ("Check: логотип в футоре")
        driver.find_element_by_xpath("//div[@class='flex footer-bottom__logo xs12 md3']")

                
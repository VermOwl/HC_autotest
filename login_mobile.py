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

# Print status
# Click
# Check
# Info
# Fill
#        print ("Click: Бургер")
#        driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
#

class hc_command_mobile():

    mail = "qwe"

    def signin(self, driver): #логиниться на helpcubes
        time.sleep(1)
        #Войти в аккаунт
        print ("Click: Бургер")
        driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
        time.sleep(1)
        print ("Click: Вход в аккаунт")
        driver.find_element_by_xpath("//a[@class='mt-4 v-btn v-btn--depressed v-btn--flat v-btn--outlined v-btn--router theme--light v-size--default primary--text']").click()

        time.sleep(2)

        #Заполнение формы ввода
        mail = self.__memory_mail()
        print("Fill: форма входа пользвоаель")
        driver.find_element_by_xpath("(//div[@class='v-input pt-5 theme--light v-text-field v-text-field--is-booted v-text-field--enclosed v-text-field--outlined']//input)").send_keys(mail)
        driver.find_element_by_xpath("(//input[@name='password'])").send_keys("23072307")

        #Войти
        print ("Click: Войти")
        driver.find_element_by_xpath("(//button[@class='v-btn v-btn--contained theme--light v-size--default'])").click()

        time.sleep(2)

        #Скипнуть момент добавления карты - Открывается главная страница
        print ("Скипнуть момент добавления карты - Открывается главная страница")
        try:
            driver.find_element_by_xpath("//button[@class='v-btn v-btn--depressed v-btn--flat v-btn--outlined theme--light v-size--default primary--text']").click()
            time.sleep(1)
        except:
            print("фывалдо")

    def setting(self, driver): #заходит в настройки пользователя
        time.sleep(2)
        print ("Click: Бургер")
        driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
        time.sleep(1)
        print("Click: Настройки пользваоеля")
        driver.find_element_by_xpath("//a[@class='profile__settings']//span").click()
        time.sleep(1)

    def setting_devices(self, driver): #открыть пользователи и устройства
        time.sleep(1)
        print ("Click: Открыть пользователи и устройства")
        driver.find_element_by_xpath("//div[@class='lk-menu-mob visible-xs']//a[2]").click()
        time.sleep(1)

    def add_devices(self, driver): #добавление устройства
        time.sleep(1)
        print ("Info: Добавление устройство для пользователя")
        print ("Click: Добавить устройствво")
        driver.find_element_by_xpath("//div[@class='container bg-white']//div[@class='flex pt-4 mt-2']//span[@class='v-btn__content']").click()    
        time.sleep(1)

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
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='v-menu__content theme--light v-menu__content--fixed menuable__content__active']//div[@class='v-list v-sheet v-sheet--tile theme--light']//div[1]//div[1]//div[1]").click()
        time.sleep(1)

        # выбор операционной систомы
        print ("Select: ОС девайса")
        elem_click = elem[1]
        elem_click.click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[contains(text(),'Windows 10')]").click()
        time.sleep(1)
        # подтверждение

        print ("Select: Сохранения устройства")
        driver.find_element_by_xpath("//button[@class='device-modal__button v-btn v-btn--contained theme--light v-size--default primary']").click()
        time.sleep(1)
        
        print("Site refresh")
        driver.refresh()
        
        time.sleep(2)
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
        time.sleep(1)

    def support_message(self,driver): #Заполениен формы отправки сообщения в службу поддержки
        
        print ("Info: Заполнение и отправки формы в ТП")
        time.sleep(1)
        #Написать в поддержку
        print ("Click: Открытие формы отправки сообщения в ТП")
        driver.find_element_by_xpath("//div[@class='text-xs-right my-auto']//button[@type='button']").click()
        time.sleep(1)

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
        driver.find_element_by_xpath("//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/div[@class='v-menu__content theme--light v-menu__content--fixed menuable__content__active']/div[@class='v-select-list v-card theme--light']/div[@class='v-list v-sheet v-sheet--tile theme--light']/div[1]/div[1]").click()
        
        #Выбор устройства из списка
        print ("Select: Устрйоство")
        elem = elem_list[1]
        elem.click()
        time.sleep(1)
        driver.find_element_by_xpath("//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/div[@class='v-menu__content theme--light v-menu__content--fixed menuable__content__active']/div[@class='v-select-list v-card theme--light']/div[@class='v-list v-sheet v-sheet--tile theme--light']/div[2]/div[1]").click()
        time.sleep(1)
        
        #Выбор пользователя из списка
        print ("Select: Пользователь")
        elem = elem_list[2]
        elem.click()
        time.sleep(1)
        driver.find_element_by_xpath("//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/div[@class='v-menu__content theme--light v-menu__content--fixed menuable__content__active']/div[@class='v-select-list v-card theme--light']/div[@class='v-list v-sheet v-sheet--tile theme--light']/div[2]/div[1]").click()
        time.sleep(1)
        
        #Добавление комментария
        print ("Fill: Описание проблемы")
        description = "Lorem ipsum dolor sit amet"
        driver.find_element_by_xpath("//textarea[@name='comment']").send_keys("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.")
        
        #Добавление файла
        print ("Fill: Добавление файла")
        driver.find_element_by_xpath("//input[@name='files[]']").send_keys("C:\\Users\\" + getpass.getuser()  + "\\Documents\\GitHub\\HC_autotest\\ford-ford-raptor-parketnik-dzhip.jpeg")
        time.sleep(1)
        
        #Нажатие кнопки отправить
        print ("Click: Отправить запрос в ТП")
        driver.find_element_by_xpath("//button[@class='v-btn v-btn--contained theme--light v-size--default primary']").click()
        time.sleep(1)

        self.check_request_jira_authorization(summary, description)

        time.sleep(1)
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
        time.sleep(1)
        print ("Info: Процедура регистрации пользователя")
        print ("Click: Бургер")
        driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
        time.sleep(1)
        print ("Click: Регистрация")
        #Неавторизованный пользовать - Регистрация
        driver.find_element_by_xpath("//a[@class='mt-2 v-btn v-btn--contained v-btn--router theme--light v-size--default primary']").click()
        time.sleep (1)

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

        time.sleep(2)

        #выход на главную
        driver.find_element_by_xpath("//button[@class='v-btn v-btn--contained theme--light v-size--default primary']").click()

        time.sleep(1)

    def getmail(self, driver): #Копируем в буфер аккаунт с сайта temp-mail.org
        time.sleep(5)
        print ("Click: Копирование текста в буфер обмена")
        driver.find_element_by_xpath("//button[@class='btn-rds icon-btn bg-theme click-to-copy copyIconGreenBtn']").click()
        self.__memory_mail()
        time.sleep(1)

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
        time.sleep(1)
        print ("Info: Добавления тариф для пользователя")
        print ("Click: Бургер")
        driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
        #Раздел: Тарифы
        
        print ("Click: Тарифы")
        driver.find_element_by_xpath("//p//a[@href='/tariffs']").click()
        time.sleep(1)

        #Выбрать второй тариф максимальный
        print ("Click: Выбрать тариф")
        elem_list = driver.find_elements_by_xpath("//button[@class='primary v-btn v-btn--contained theme--light v-size--default']")
        elem = elem_list[2]
        elem.click()
        time.sleep(1)

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

        time.sleep(1)

    def signin_parametr(self, driver, login, password): #Вход со своими параметрами 
        
        print ("Info: вход с параметрами " + login + " " +  password)
        print ("Click: Бургер")
        driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
        time.sleep(1)
        #Войти в аккаунт
        print ("Click: Вход в аккаунт")
        driver.find_element_by_xpath("(//a[@class='mt-4 v-btn v-btn--depressed v-btn--flat v-btn--outlined v-btn--router theme--light v-size--default primary--text'])").click()

        time.sleep(2)

        #Заполнение формы ввода
        print ("Fill: mail")
        driver.find_element_by_xpath("(//div[@class='v-input pt-5 theme--light v-text-field v-text-field--is-booted v-text-field--enclosed v-text-field--outlined']//input)").send_keys(login)
        print ("Fill: pass")
        driver.find_element_by_xpath("(//input[@name='password'])").send_keys(password)

        #Войти
        print ("Click: Вход после заполения полей")
        driver.find_element_by_xpath("(//button[@class='v-btn v-btn--contained theme--light v-size--default'])").click()

        time.sleep(2)

        #Скипнуть момент добавления карты - Открывается главная страница
        try:
            driver.find_element_by_xpath("//button[@class='v-btn v-btn--depressed v-btn--flat v-btn--outlined theme--light v-size--default primary--text']").click()
            time.sleep(1)
        except:
            print("фывалдо")

    def add_profile_info(self, driver): #Заполнение информации о пользваотеле


        time.sleep(1)
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
        time.sleep(1)
        print ("Click: Установить женский пол")
        elem = driver.find_elements_by_xpath("//div[@class='v-input--selection-controls__ripple']")
        elem_click = elem[1]
        elem_click.click()
        time.sleep(0.4)
        # Изменение номера телефона
        print ("Fill: Установить номер телефона")
        driver.find_element_by_xpath("//input[@placeholder='+7 (###) ###-##-##']").send_keys("1234567890")     
        time.sleep(1)
        # Сохранить изменения
        print ("Click: Сохранить")
        driver.find_element_by_xpath("//button[@class='v-btn v-btn--block v-btn--contained theme--light v-size--default primary']").click()

        time.sleep(1)
        # Обновить страницу
        
        driver.refresh()
        time.sleep(1)

        # Проверка изменений 
        print ("Info: Проверка добаленной информации")
        print ("Check: Фамилия")
        driver.find_element_by_xpath("//input[@value='" + last_name + "']")
        print ("Check: Пол")
        driver.find_element_by_xpath("//div[@class='v-radio theme--light v-item--active']//input[@value='female']")
        print ("Check: Номер телефона")
        driver.find_element_by_xpath("//input[@value='+7 (123) 456-78-90']")
        
        time.sleep(1)

    def add_user(self, driver): #добавление юзера в настройках пользователя
        time.sleep(1)
        #Открыть форму добавления пользвоателя
        print ("Info: Добавление юзера в аккаунт пользователя")
        print ("Click: Добавить пользователя")
        driver.find_element_by_xpath("//div[@class='container bg-white']//div[@class='flex pt-4 mt-2 pb-2']//button[@class='v-btn v-btn--contained theme--light v-size--default secondary']").click()
        time.sleep(1)

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
        time.sleep(1)
        #Сохранить изменения 
        print ("Click: Сохранить изменения")
        driver.find_element_by_xpath("//button[@class='users-modal__button v-btn v-btn--contained theme--light v-size--default primary']").click()
        
        time.sleep(1)
        driver.refresh()
        time.sleep(2)

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
        time.sleep(1)

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
        time.sleep(1)
        print ("Click: Бургер")
        driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()
        # Открыть контакты
        print ("Click: Открыть страницу Контакты")
        driver.find_element_by_xpath("//p[@class='header__link']//a[@href='/contacts']").click()
        time.sleep(1)

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
        description = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum"
        driver.find_element_by_xpath("//textarea[@aria-label='Ваше сообщение']").send_keys(description)
        
        # Отправить запрос 
        print ("Click: Отправить запрос")
        driver.find_element_by_xpath("//button[@type='submit']").click()

        self.chech_request_jira(mail, phone, name, description)
        
        # Кнопка Спассибо
        time.sleep(1)
        print ("Click: Спасибо")
        driver.find_element_by_xpath("//button[@class='green-btn text-xs-left v-btn v-btn--contained theme--light v-size--default']").click()

        print("Отправка запроса по форме отбраной связи успешно завершена")        

    def chech_request_jira(self, mail, phone, name, description): #Проверка на приход информации в jira при запросе в ТП от неавторизованного пользвоателя
        
        print("Info: Запущена проверка прихода запросов в JIRA")
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://jira.bsr.group/projects/CSUP/queues/custom/")
        time.sleep(1)

        # Вход в аккаунт
        print ("Fill: Логин Jira")
        driver.find_element_by_xpath("//input[@id='login-form-username']").send_keys("vermowl")
        print ("Fill: Пароль Jira")
        driver.find_element_by_xpath("//input[@id='login-form-password']").send_keys("9575344GHty")
        print ("Click: Логин")
        driver.find_element_by_xpath("//input[@id='login-form-submit']").click()
        time.sleep(1.5)

        # Открытие первой найденной задачи 
        print ("Click: Открытие первой найденной задачи")
        elem = driver.find_elements_by_xpath("//a[@class='issue-link']")
        elem_click = elem[0]
        elem_click.click()
        time.sleep(2)

        # Проверка контента 
        print ("Check: mail")
        driver.find_element_by_xpath("//a[contains(text(),'" + mail + "')]")
        print ("Check: phone number")
        driver.find_element_by_xpath("//div[contains(text(),'+7 (123) 456-78-90')]")
        print ("Check: Name")
        driver.find_element_by_xpath("//div[contains(text(),'" + name + "')]")
        print ("Check: Description")
        driver.find_element_by_xpath("//p[contains(text(),'" + description + "')]")
        time.sleep(1)
        print("Info: Запросы успешно найден и проверен в JIRA")

        driver.quit()

    def check_request_jira_authorization(self, summary, description): #Проверка на приход заявок в JIRA от авторизованног пользователя 
        
        print("Info: Запущена проверка прихода запросов в JIRA от авторизованного пользователя")

        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://jira.bsr.group/projects/CSUP/queues/custom/")
        time.sleep(1)

        # Вход в аккаунт
        print ("Fill: Логин Jira")
        driver.find_element_by_xpath("//input[@id='login-form-username']").send_keys("vermowl")
        print ("Fill: Пароль Jira")
        driver.find_element_by_xpath("//input[@id='login-form-password']").send_keys("9575344GHty")
        print ("Click: Логин")
        driver.find_element_by_xpath("//input[@id='login-form-submit']").click()
        time.sleep(1.5)

        # Открытие первой найденной задачи 
        print ("Click: Открытие первой найденной задачи")
        elem = driver.find_elements_by_xpath("//a[@class='issue-link']")
        elem_click = elem[0]
        elem_click.click()
        time.sleep(2)

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
        time.sleep(1)
        print ("Info: Открыть форму логина")
        
        print ("Click: Бургер")
        driver.find_element_by_xpath("//i[@class='v-icon material-icons theme--dark']").click()

        print ("Click: Вход")
        driver.find_element_by_xpath("//span[@class='v-btn__content'][contains(text(),'Вход')]").click()
        
        time.sleep(1)

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

    
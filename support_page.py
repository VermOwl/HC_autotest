from login import hc_command
import configparser


def support_page(driver):
    test = hc_command()

    config = configparser.ConfigParser()
    config.read('config.ini')
    email = config['USER INFO']['email']
    password = "23072307"

    driver.get(test.site() + "/support")
    driver.implicitly_wait(10)

    test.signin_parametr(driver, email, password)    
    

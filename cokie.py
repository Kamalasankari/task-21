from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


class Cokie:
    def __init__(self):
        self.url = "https://www.saucedemo.com/"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        try:
            self.driver.maximize_window()
            sleep(4)
            self.driver.get(self.url)
            sleep(4)
            print("Cookies before Login: ",self.driver.get_cookies())
            self.driver.find_element(by=By.ID, value="user-name").send_keys("standard_user")
            sleep(4)
            self.driver.find_element(by=By.ID, value="password").send_keys("secret_sauce")
            sleep(4)
            self.driver.find_element(by=By.ID, value="login-button").click()
            sleep(4)
            print("Cookies after Login: ", self.driver.get_cookies())
        except:
            print("Login Failed")
        finally:
            self.driver.close()
c = Cokie()
c.login()


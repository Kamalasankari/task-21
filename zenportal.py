from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class Zenportal:
    def __init__(self):
        self.url = "https://www.zenclass.in/login/"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(4)
            self.driver.find_element(by=By.NAME, value="email").send_keys("Kamalasankari@gmail.com")
            sleep(4)
            self.driver.find_element(by=By.NAME, value="password").send_keys("K@mala0306")
            sleep(4)
            self.driver.find_element(by=By.TAG_NAME, value="Button").click()
            sleep(4)
            a = ActionChains(self.driver)
            m = self.driver.find_element(by=By.XPATH, value="//*[@id='root']/div[1]/nav")
            sleep(4)
            a.move_to_element(m).perform()
            self.driver.find_element(by=By.XPATH, value="//*[@id='root']/div[1]/nav/ul/div[2]/li/span/div/div[2]").click()
            sleep(4)
            n = self.driver.find_element(by=By.XPATH, value="//img[@class='profileIcon']")
            a.move_to_element(n).click(n).perform()
            self.driver.find_element(by=By.XPATH, value="//*[@id='root']/nav/div/div/div/div/button[2]").click()
            sleep(4)

        except NoSuchElementException as selenium_error:
            print(selenium_error)
        finally:
            self.driver.close()
c=Zenportal()
c.login()

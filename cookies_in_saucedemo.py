
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Saucedemo_cookies:

#initialysing driver and url
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

#open the url
    def display_cookies_before_login(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        print("cookies before login")
        for cookies in self.driver.get_cookies():
            print(cookies)

#login into the url and fetch the cookies
    def login_function(self):
        user_name = self.driver.find_element(By.ID, "user-name")
        user_name.send_keys(self.username)
        time.sleep(5)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(self.password)
        time.sleep(5)
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        time.sleep(5)
        print("cookies after login")
        for cookies in self.driver.get_cookies():
            print(cookies)

#execution path for calling each functions in the class

if __name__ == "__main__":
    url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    result = Saucedemo_cookies(url, username,password)
    result.display_cookies_before_login()
    result.login_function()


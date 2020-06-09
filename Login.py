from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import TimeoutException

import Setup


class Login:

    def __init__(self):
        self.email = Setup.EMAIL
        self.password = Setup.PASSWORD
        self.browser = webdriver.Chrome(executable_path=Setup.CHROME_PATH)

    def get_website(self):
        url = 'https://www.instagram.com/accounts/login/?hl=en'
        self.browser.get(url)

    def login(self):
        try:
            wait = WebDriverWait(self.browser, 10)
            wait.until(EC.presence_of_element_located((By.NAME, 'username')))
            wait.until(EC.presence_of_element_located((By.NAME, 'password')))
        finally:
            pass

        email_box = self.browser.find_element_by_name('username')
        password_box = self.browser.find_element_by_name('password')
        email_box.send_keys(self.email)
        password_box.send_keys(self.password)

        password_box.send_keys(Keys.ENTER)

    def manage_save(self):
        wait = WebDriverWait(self.browser, 30)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        identify = self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
        identify.click()

    def manage_note(self):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        identify = self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
        identify.click()

    def login_to_insta(self):
        self.get_website()
        self.login()
        self.manage_save()
        try:
            self.manage_note()
        except TimeoutException as e:
            print(e)
        sleep(10)


if __name__ == '__main__':
    new_login = Login()
    new_login.login_to_insta()
    new_login.browser.quit()

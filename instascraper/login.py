from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

import setup
from instascraper.scraper_interface import ScraperInterface
from instascraper.scrape_info import GetNumbers


class LogIn(ScraperInterface):

    def __init__(self):
        self.email = setup.EMAIL
        self.password = setup.PASSWORD
        print(setup.CHROME_PATH)
        self.browser = webdriver.Chrome(executable_path=setup.CHROME_PATH)

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

    def main(self):
        self.get_website()
        self.login()
        self.manage_save()
        try:
            self.manage_note()
        except TimeoutException as e:
            print(e)
        sleep(5)
        GetNumbers(self.browser).main()
        return 'Logged in into your account'


if __name__ == '__main__':
    # new_login = LogIn()
    # new_login.main()
    # new_login.browser.quit()

    pass

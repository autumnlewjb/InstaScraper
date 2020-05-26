from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
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
        email_box = self.browser.find_element_by_name('username')
        password_box = self.browser.find_element_by_name('password')
        email_box.send_keys(self.email)
        password_box.send_keys(self.password)

        password_box.send_keys(Keys.ENTER)

    def manage_save(self):
        options = self.browser.find_elements_by_tag_name('button')
        if Setup.SAVE_LOGIN:
            options[0].click()
        else:
            options[1].click()

    def manage_note(self):
        accept = None
        reject = None
        while True:
            try:
                accept = self.browser.find_element_by_xpath('//button[@class="aOOlW  bIiDR  "]')
                reject = self.browser.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]')
                break
            except NoSuchElementException:
                sleep(5)
                continue

        if Setup.TURN_ON_NOTE:
            accept.click()
        else:
            reject.click()

    def login_to_insta(self):
        self.get_website()
        sleep(5)
        self.login()
        sleep(5)
        try:
            self.manage_save()
            sleep(1)
        except NoSuchElementException:
            pass
        self.manage_note()
        sleep(10)


if __name__ == '__main__':
    new_login = Login()
    new_login.login_to_insta()

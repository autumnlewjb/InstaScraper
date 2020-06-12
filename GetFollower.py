import time

from Login import Login
import Setup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import re


def filter_li(tag):
    if tag.name == 'ul' and len(tag.contents) == 3:
        return True
    else:
        return False


class GetFollower:

    def __init__(self, browser):
        self.browser = browser
        self.soup = None

    def _wait(self, element, means='xpath'):
        wait = WebDriverWait(self.browser, 30)
        if means == 'xpath':
            wait.until(EC.presence_of_element_located((By.XPATH, str(element))))
        elif means == 'class':
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, str(element))))

    def homepage(self):
        self._wait("//a[@href='/']")
        self.browser.find_element_by_xpath("//a[@href='/']").click()

    def profile(self):
        self._wait("//a[@href='/{}/']".format(Setup.CURRENT_USERNAME))
        self.browser.find_element_by_xpath("//a[@href='/{}/']".format(Setup.CURRENT_USERNAME)).click()
        self._wait("k9GMp", 'class')

    def make_soup(self):
        source = self.browser.page_source
        self.soup = bs(source, 'lxml')
        # print(self.soup.prettify())

    def get_numbers(self):
        ul = self.soup.find('ul', class_='k9GMp')
        for element in ul.children:
            print(element.get_text())

    def follower_list(self):
        self._wait("//a[@href='/{}/followers/']".format(Setup.CURRENT_USERNAME))
        self.browser.find_element_by_xpath("//a[@href='/{}/followers/']".format(Setup.CURRENT_USERNAME)).click()
        time.sleep(10)
        self.make_soup()

    # TODO: this sometimes don't work check this later (might be due to the sleep)
    def print_list(self):
        div = self.soup.find_all('li', class_='wo9IH')
        print(len(div))
        for child in div:
            print(child.find_all('a', href='d7ByH').get_text())

        # for li in div:
        #     print(li.get_text())


if __name__ == '__main__':
    new_login = Login()
    new_login.login_to_insta()
    get_follower = GetFollower(new_login.browser)
    get_follower.homepage()
    get_follower.profile()

    # get_follower.make_soup()
    # get_follower.get_numbers()
    # get_follower.browser.quit()

    get_follower.follower_list()
    get_follower.print_list()

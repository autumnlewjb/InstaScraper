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

    def _get_numbers(self):
        self.make_soup()
        ul = self.soup.find('ul', class_='k9GMp')
        numbers = dict()
        for element in ul.children:
            text = element.get_text()
            if not text:
                pass
            elif re.search('post', text):
                numbers['post'] = int(text.split(' ')[0])
            elif re.search('follower', text):
                numbers['follower'] = int(text.split(' ')[0])
            elif re.search('following', text):
                numbers['following'] = int(text.split(' ')[0])

        return numbers

    def _follower_list(self):
        self._wait("//a[@href='/{}/followers/']".format(Setup.CURRENT_USERNAME))
        self.browser.find_element_by_xpath("//a[@href='/{}/followers/']".format(Setup.CURRENT_USERNAME)).click()
        # time.sleep(30)

        flag = list()
        count = 0

        while len(flag) != Setup.DETAILS['follower']:
            flag = self.browser.find_elements_by_xpath("//div[@class='d7ByH']")
            time.sleep(2)
            count += 1
            if count % 20 == 0:
                self.browser.refresh()
                self._wait("//a[@href='/{}/followers/']".format(Setup.CURRENT_USERNAME))
                self.browser.find_element_by_xpath("//a[@href='/{}/followers/']".format(Setup.CURRENT_USERNAME)).click()

        self.make_soup()

    def _following_list(self):
        self._wait("//a[@href='/{}/following/']".format(Setup.CURRENT_USERNAME))
        self.browser.find_element_by_xpath("//a[@href='/{}/following/']".format(Setup.CURRENT_USERNAME)).click()
        # time.sleep(30)
        flag = list()
        count = 0
        # TODO: the calling of the method get_numbers is causing infinite loop
        while len(flag) != Setup.DETAILS['following']:
            flag = self.browser.find_elements_by_xpath("//div[@class='d7ByH']")
            time.sleep(2)
            count += 1
            if count % 20 == 0:
                self.browser.refresh()
                self._wait("//a[@href='/{}/followers/']".format(Setup.CURRENT_USERNAME))
                self.browser.find_element_by_xpath("//a[@href='/{}/followers/']".format(Setup.CURRENT_USERNAME)).click()

        self.make_soup()

    def _print_list(self):
        div = self.soup.find_all('div', class_='d7ByH')
        result = [element.get_text() for element in div]
        # print(len(div))
        # for element in div:
        #     print(element.get_text())
        print(result)
        return result

    def confirm_number(self):
        print(len(self.soup.find('div', class_='PZuss').contents))

    def follower_list(self):
        self.homepage()
        self.profile()
        print('follower')

        self._follower_list()
        self.browser.refresh()
        return self._print_list()

    def following_list(self):
        self.homepage()
        self.profile()
        print('following')

        self._following_list()
        self.browser.refresh()
        return self._print_list()

    def no_friend_list(self):
        print('running this')
        followers = self.follower_list()
        followings = self.following_list()
        return [following for following in followings if following not in followers]

    def get_numbers(self):
        self.homepage()
        self.profile()
        print('this is the problem')
        Setup.DETAILS = self._get_numbers()
        return Setup.DETAILS


if __name__ == '__main__':
    new_login = Login()
    new_login.login_to_insta()
    get_follower = GetFollower(new_login.browser)
    get_follower.homepage()
    get_follower.profile()

    # print(get_follower.follower_list())
    # print(get_follower.following_list())
    # print(get_follower.no_friend_list())
    # for x, y in get_follower.get_numbers().items():
    #     print(x, y)

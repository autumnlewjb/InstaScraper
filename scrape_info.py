import time

# from login import LogIn
import setup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import re
import subprocess as sub
from tkinter import *
import os
from insta_scraper import InstaScraper


def filter_li(tag):
    if tag.name == 'ul' and len(tag.contents) == 3:
        return True
    else:
        return False


class GetFollower(InstaScraper):
    def __init__(self, browser):
        self.browser = browser
        self.soup = None

    def _wait(self, element, means='xpath'):
        wait = WebDriverWait(self.browser, 30)
        if means == 'xpath':
            wait.until(EC.element_to_be_clickable((By.XPATH, str(element))))
        elif means == 'class':
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, str(element))))

    def homepage(self):
        self.browser.implicitly_wait(10)
        self._wait("//a[@href='/']")
        self.browser.find_element_by_xpath("//a[@href='/']").click()
        self.browser.implicitly_wait(10)

    def profile(self):
        self._wait("//a[@href='/{}/']".format(setup.CURRENT_USERNAME))
        self.browser.find_element_by_xpath("//a[@href='/{}/']".format(setup.CURRENT_USERNAME)).click()
        self._wait("k9GMp", 'class')

    def make_soup(self):
        source = self.browser.page_source
        self.soup = bs(source, 'lxml')
        # print(self.soup.prettify())

    def _follower_list(self):
        self._wait("//a[@href='/{}/followers/']".format(setup.CURRENT_USERNAME))
        self.browser.find_element_by_xpath("//a[@href='/{}/followers/']".format(setup.CURRENT_USERNAME)).click()
        # time.sleep(30)

        flag = list()
        tmp = 0
        count = 0

        while len(flag) < setup.DETAILS['follower']:
            tmp = len(flag)
            self._wait("/html/body/div[4]/div/div/div[2]")
            scroll_box = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
            self.browser.execute_script(
                    "arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;",
                    scroll_box)
            flag = self.browser.find_elements_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li")
            if len(flag) == tmp:
                count += 1
            time.sleep(2)
            if count % 20 == 0:
                self.browser.refresh()
                self._wait("//a[@href='/{}/followers/']".format(setup.CURRENT_USERNAME))
                self.browser.find_element_by_xpath("//a[@href='/{}/followers/']".format(setup.CURRENT_USERNAME)).click()

            print(len(flag))

        self.make_soup()

    def _print_list(self):
        div = self.soup.find_all('div', class_='d7ByH')
        result_list = [element.a.get_text() for element in div if not element.find('span', string='Verified')]
        # print(len(div))
        for element in div:
            print(element.get_text())
        # print(result_list)
        return result_list

    def confirm_number(self):
        print(len(self.soup.find('div', class_='PZuss').contents))

    def main(self):
        self.profile()
        self._follower_list()
        self.browser.refresh()
        return self._print_list()


class GetFollowing(GetFollower):
    def _following_list(self):
        self._wait("//a[@href='/{}/following/']".format(setup.CURRENT_USERNAME))
        self.browser.find_element_by_xpath("//a[@href='/{}/following/']".format(setup.CURRENT_USERNAME)).click()
        # time.sleep(30)
        flag = list()
        tmp = 0
        count = 0

        while len(flag) < setup.DETAILS['following']:
            tmp = len(flag)
            self._wait("/html/body/div[4]/div/div/div[2]")
            scroll_box = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
            self.browser.execute_script(
                "arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;",
                scroll_box)
            flag = self.browser.find_elements_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li")
            if len(flag) == tmp:
                count += 1
            time.sleep(2)
            if count % 20 == 0:
                self.browser.refresh()
                self._wait("//a[@href='/{}/following/']".format(setup.CURRENT_USERNAME))
                self.browser.find_element_by_xpath("//a[@href='/{}/following/']".format(setup.CURRENT_USERNAME)).click()

            print(len(flag))

        self.make_soup()

    def main(self):
        self.profile()
        self._following_list()
        self.browser.refresh()
        return self._print_list()


class GetNumbers(GetFollower):
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

    def main(self):
        self.profile()
        print('this is the problem')
        setup.DETAILS = self._get_numbers()
        self.homepage()
        return setup.DETAILS


class NoFriend(GetFollowing, GetFollower):
    def main(self):
        followers = GetFollower(self.browser).main()
        followings = GetFollowing(self.browser).main()
        setup.NO_FRIEND_LIST = [following for following in followings if following not in followers]
        return setup.NO_FRIEND_LIST


if __name__ == '__main__':
    # only import when you need it (circular import)
    # login = LogIn()
    # login.main()
    #
    # # This must run first
    #
    # get_follower = GetFollower(login.browser)
    # get_follower.result_gui()
    #
    # get_following = GetFollowing(login.browser)
    # get_following.result_gui()
    #
    # # no_friend_list = NoFriend(login.browser)
    # # no_friend_list.result_gui()

    pass

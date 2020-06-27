import time

import setup
from scrape_info import NoFriend
from login import LogIn
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Unfollowing(NoFriend):
    def main(self):
        return_status = list()
        unfollow_list = setup.NO_FRIEND_LIST
        if not unfollow_list:
            unfollow_list = NoFriend(self.browser).main()

        # self._wait("//a[@href='/{}/following/']".format(CURRENT_USERNAME))
        # self.browser.find_element_by_xpath("//a[@href='/{}/following/']".format(CURRENT_USERNAME)).click()
        if unfollow_list:
            for username in unfollow_list:
                xpath = "//a[contains(text(), '{}')]/../../../..//button[contains(text(), 'Following')]".format(username)
                print(xpath)
                self._wait(xpath)
                self.browser.find_element_by_xpath(xpath).click()
                # self._wait("//button[contains(text(), 'Unfollow')]")
                # unfollow_button = self.browser.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
                self._wait("//button[contains(text(), 'Cancel')]")
                cancel = self.browser.find_element_by_xpath("//button[contains(text(), 'Cancel')]").click()
                return_status.append('Unfollowed {}'.format(username))

        return return_status


if __name__ == '__main__':
    # new_login = LogIn()
    # new_login.main()
    #
    # unfollow = Unfollowing(new_login.browser)
    # unfollow.main()
    pass

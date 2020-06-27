from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import ElementNotInteractableException
from login import LogIn
from time import sleep
from selenium.webdriver.common.keys import Keys

from logout import LogOut
from setup import PAGE_DOWN_TIME
from insta_scraper import InstaScraper


def check_parent(tag):
    result = True
    parents = [str(i.name) for i in tag.parents]
    # print(parents)
    for parent in parents:
        if parent == 'header':
            result = False
            break
        else:
            continue

    if result:
        return tag
    else:
        return None


count = 0


class GetImageLink:

    def __init__(self, browser):
        self.browser = browser
        self.soup = None
        self.links = []
        self.get_link()

    def create_soup(self):
        source = self.browser.page_source
        soup = bs(source, 'lxml')

        return soup

    def scroll_down(self):
        doc = self.soup.html
        try:
            element = self.browser.find_element_by_tag_name('body')
            element.send_keys(Keys.PAGE_DOWN)
        except ElementNotInteractableException:
            for child in doc.descendants:
                try:
                    if child.name is not None:
                        element = self.browser.find_element_by_tag_name(str(child.name))
                        element.send_keys(Keys.PAGE_DOWN)
                        print('Scrolled Down')
                        print(child.name)
                        break
                except ElementNotInteractableException:
                    continue

    def get_link_each(self):
        locate = self.soup.find('div', class_='zGtbP IPQK5 VideM')
        tmp = None
        try:
            tmp = locate.next_sibling.find_all('img')
        except AttributeError:
            print(self.soup.encode('utf-8'))
        want = [check_parent(tag) for tag in tmp]
        link = [each.get('src') for each in want if each is not None]

        return link

    def get_link(self):
        global count
        self.soup = self.create_soup()
        links = self.get_link_each()
        for link in links:
            if link not in self.links:
                self.links.append(link)
        count += 1
        print(len(self.links))
        if count < PAGE_DOWN_TIME:
            self.scroll_down()
            self.get_link()
        elif len(self.links) == 0:
            self.browser.find_element_by_tag_name('body').send_keys(Keys.HOME)
            sleep(5)
            count = 0
            self.get_link()
        else:
            LogOut(self.browser).main()
            print(self.links)


if __name__ == '__main__':
    # new_login = LogIn()
    # new_login.main()
    # get_image = GetImageLink(new_login.browser)
    # sleep(5)
    # print(get_image.links)
    # print(len(get_image.links))

    pass

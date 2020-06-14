import io
from time import sleep

import requests
from PIL import Image
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys

import Setup
from FileManager import FileManager
from InstaScraper import InstaScraper
from Login import LogIn
from Logout import LogOut
from Setup import PAGE_DOWN_TIME


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


class DownloadImage(InstaScraper):

    def __init__(self, browser):
        self.browser = browser
        self.soup = None
        self.links = []
        self.get_link()
        self.byte = self.fetch_image()

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

    def fetch_image(self):
        complete = []
        print(self.links)

        req = [requests.get(lk) for lk in self.links]
        print('this is run')
        in_byte = [io.BytesIO(request.content) for request in req]
        print('this is run')
        # import pdb; pdb.set_trace()
        complete.extend(in_byte)

        return complete

    def main(self):
        for image in self.byte:
            new_image = Image.open(image)
            new_file = FileManager()
            with open(new_file.filename(), 'wb') as fp:
                new_image.save(fp)
                # fp.close()
        return 'All image saved in the directory: ' + Setup.SAVE_PATH


if __name__ == '__main__':
    new_login = LogIn()
    new_login.main()
    obj = DownloadImage(new_login.browser)
    obj.result_gui()

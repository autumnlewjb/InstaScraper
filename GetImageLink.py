from bs4 import BeautifulSoup as bs
from Login import Login
from time import sleep
from selenium.webdriver.common.keys import Keys
import numpy


def check_parent(tag):
    # import pdb; pdb.set_trace()
    result = True
    parents = [str(i.name) for i in tag.parents]
    print(parents)
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


num_of_elements = 0


class GetImageLink:

    def __init__(self, browser):
        self.browser = browser
        self.soup = [self.create_soup() for _ in range(10) if self.create_soup() is not None]
        self.links = self.get_link()

    def create_soup(self):
        source = self.browser.page_source
        soup = bs(source, 'lxml')
        self.scroll_down()

        if soup not in self.soup:
            return soup
        else:
            return None

    def scroll_down(self):
        element = self.browser.find_element_by_tag_name('div')
        element.send_keys(Keys.PAGE_DOWN)

    def get_link_each(self, count):
        locate = self.soup[count].find('div', class_='zGtbP IPQK5 VideM')
        tmp = locate.next_sibling.find_all('img')
        want = [check_parent(tag) for tag in tmp]
        link = [each.get('src') for each in want if each is not None]
        print(link)
        count += len(link)
        print(count)

        return link

    def get_link(self):
        link = []
        for i in range(len(self.soup)):
            tmp = self.get_link_each(i)
            link.extend(tmp)

        return link

    def get_image_link(self):
        pass


if __name__ == '__main__':
    new_login = Login()
    new_login.login_to_insta()
    get_image = GetImageLink(new_login.browser)
    sleep(5)
    print(get_image.links)
    print(len(get_image.links))

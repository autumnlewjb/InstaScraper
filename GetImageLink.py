from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import ElementNotInteractableException
from Login import Login
from time import sleep
from selenium.webdriver.common.keys import Keys


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
        self.soups = []
        # self.soups = [self.create_soup() for _ in range(10) if self.create_soup() is not None]

        for _ in range(10):
            # import pdb; pdb.set_trace()
            if self.create_soup() is not None:
                self.soups.append(self.create_soup())

        print(len(self.soups))
        self.links = self.get_link()

    def create_soup(self):
        source = self.browser.page_source
        soup = bs(source, 'lxml')
        self.scroll_down(soup)
        # import pdb; pdb.set_trace()

        if soup not in self.soups:
            return soup
        else:
            return None

    def scroll_down(self, soup):
        doc = soup.html
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

    def get_link_each(self, count):
        locate = self.soups[count].find('div', class_='zGtbP IPQK5 VideM')
        import pdb; pdb.set_trace()
        tmp = locate.next_sibling.find_all('img')
        want = [check_parent(tag) for tag in tmp]
        link = [each.get('src') for each in want if each is not None]
        print(link)
        count += len(link)
        print(count)

        return link

    def get_link(self):
        link = []
        for i in range(len(self.soups)):
            import pdb; pdb.set_trace()
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

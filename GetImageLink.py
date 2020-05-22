from bs4 import BeautifulSoup as bs
from Login import Login
from time import sleep


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


class GetImageLink:

    def __init__(self, browser):
        self.browser = browser
        self.soup = self.create_soup()
        self.links = self.get_link()

    def create_soup(self):
        source = self.browser.page_source
        soup = bs(source, 'lxml')

        return soup

    def get_link(self):
        locate = self.soup.find('div', class_='zGtbP IPQK5 VideM')
        tmp = locate.next_sibling.find_all('img')
        want = [check_parent(tag) for tag in tmp]
        link = [each.get('src') for each in want if each is not None]
        print(link)

        return link

    def get_image_link(self):
        pass


if __name__ == '__main__':
    new_login = Login()
    new_login.login_to_insta()
    get_image = GetImageLink(new_login.browser)
    sleep(5)
    image_links = get_image.get_link()

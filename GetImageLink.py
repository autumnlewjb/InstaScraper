from bs4 import BeautifulSoup as bs
from Login import Login


def check_parent(tag):
    # import pdb; pdb.set_trace()
    result = True
    for parent in tag.parents:
        if parent.name == 'header':
            result = False
            break
        else:
            continue

    if result:
        return tag
    else:
        return None


class GetImageLink(Login):

    def __init__(self, browser):
        self.browser = browser

    def create_soup(self):
        source = self.browser.page_source
        soup = bs(source, 'lxml')

        return soup

    def get_link(self):
        soup = self.create_soup()
        locate = soup.find('div', class_='zGtbP IPQK5 VideM')
        tmp = locate.next_sibling.find_all('img')
        want = [check_parent(tag) for tag in tmp]
        link = [each.get('src') for each in tmp if each is not None]
        print(link)

        return link

    def get_image_link(self):
        new_login = Login()
        new_login.login_to_insta()
        get_image = GetImageLink(new_login.browser)
        get_image.get_link()


if __name__ == '__main__':
    pass

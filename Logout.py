from Setup import CURRENT_USERNAME
from InstaScraper import InstaScraper


class LogOut(InstaScraper):
    def __init__(self, browser):
        self.browser = browser

    def main(self):
        url = "https://www.instagram.com/{}/".format(CURRENT_USERNAME)
        self.browser.get(url)
        settings_button = self.browser.find_element_by_class_name("wpO6b ")
        settings_button.click()
        log_out_buttons = self.browser.find_elements_by_xpath("//button[@class = 'aOOlW   HoLwm ']")
        count = 0
        for x in log_out_buttons:
            count += 1
            if count == 9:
                x.click()
                break

        self.browser.quit()
        return 'Logged out from your Instagram account'

from Setup import CURRENT_USERNAME


def log_out(browser):
    url = "https://www.instagram.com/{}/".format(CURRENT_USERNAME)
    browser.get(url)
    settings_button = browser.find_element_by_class_name("wpO6b ")
    settings_button.click()
    log_out_buttons = browser.find_elements_by_xpath("//button[@class = 'aOOlW   HoLwm ']")
    count = 0
    for x in log_out_buttons:
        count += 1
        if count == 9:
            x.click()
            break

# this python file is for the setup
import os

EMAIL = ''
PASSWORD = ''
CURRENT_USERNAME = ''

DETAILS = dict()
NO_FRIEND_LIST = list()

SAVE_LOGIN = False
TURN_ON_NOTE = False

CHROME_PATH = os.getcwd() + r'\chromedriver.exe'
SAVE_PATH = os.path.split(os.getcwd())[0] + r'\InstaImage'
print(CHROME_PATH, SAVE_PATH)

PAGE_DOWN_TIME = 15

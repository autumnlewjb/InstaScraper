from Login import Login
from DownloadImage import DownloadImage

if __name__ == '__main__':
    # Login to user's Instagram account
    new_login = Login()
    new_login.login_to_insta()

    # get all image links
    download = DownloadImage(new_login.browser)
    download.save_image()

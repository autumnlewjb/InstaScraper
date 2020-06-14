from GUI import intro_gui, details_gui
from Login import Login
from GetFollower import GetFollower
from Logout import log_out
from DownloadImage import DownloadImage


if __name__ == '__main__':
    # Get user's information
    intro_gui()

    # Login to user's Instagram account
    new_login = Login()
    new_login.login_to_insta()

    # Get numbers
    new_get = GetFollower(new_login.browser)
    user_option = details_gui(new_get.get_numbers())
    new_get.homepage()

    if user_option == 1:
        log_out(new_login.browser)
    elif user_option == 2:
        # get all image links
        download = DownloadImage(new_login.browser)
        download.save_image()
    elif user_option == 3:
        print(new_get.follower_list())
    elif user_option == 4:
        print(new_get.following_list())
    elif user_option == 5:
        the_list = new_get.no_friend_list()
        print(the_list)
        print(len(the_list))

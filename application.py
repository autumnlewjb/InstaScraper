from gui import intro_gui, details_gui
from login import LogIn
from scrape_info import GetFollower, GetFollowing, GetNumbers, NoFriend
from logout import LogOut
from scrape_image import DownloadImage
from unfollowing import Unfollowing


if __name__ == '__main__':
    # Get user's information
    intro_gui()

    # Login to user's Instagram account
    new_login = LogIn()
    new_login.main()

    # Get numbers of posts, follower and following
    numbers = GetNumbers(new_login.browser).main()

    # Get user input
    user_input = details_gui(numbers)

    if user_input == 1:
        # Log out from the account
        LogOut(new_login.browser).result_gui()
    elif user_input == 2:
        # Scrape image
        DownloadImage(new_login.browser).result_gui()
    elif user_input == 3:
        # Get a list of followers
        GetFollower(new_login.browser).result_gui()
    elif user_input == 4:
        # Get a list of following
        GetFollowing(new_login.browser).result_gui()
    elif user_input == 5:
        # Get a list of those who you followed but they don't follow you back
        NoFriend(new_login.browser).result_gui()
    elif user_input == 6:
        # Unfollow those who don't follow you back
        # Run NoFriend first if NoFriend is not run before hand
        Unfollowing(new_login.browser).result_gui()

    new_login.browser.quit()

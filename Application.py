from GUI import intro_gui, details_gui
from Login import LogIn
from ScrapeInfo import GetFollower, GetFollowing, GetNumbers, NoFriend
from Logout import LogOut
from ScrapeImage import DownloadImage


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

    new_login.browser.quit()

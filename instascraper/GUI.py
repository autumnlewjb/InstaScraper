from tkinter import *
import setup
from ctypes import windll
from instascraper.menu import menu

email = None
username = None
password = None
save = 0

windll.shcore.SetProcessDpiAwareness(1)


class Gui(Tk):
    def close_intro(self):
        self.destroy()
        basic_info()

    def close_info(self):
        global email, username, password, save
        self.destroy()
        email = email.get()
        username = username.get()
        password = password.get()
        write_info()
        print(email, username, password)
        # save_note()

    def save(self):
        global save
        self.destroy()
        save = 1

    def dont_save(self):
        global save
        self.destroy()
        save = 0


def intro():
    root = Gui()
    root.title('Get Started')

    label = Label(text='Get Started')
    label.pack()

    button = Button(text='OK', command=root.close_intro)
    button.pack()
    root.mainloop()


def basic_info():
    global email, username, password
    read_info()
    root = Gui()
    root.title('Login Information')

    email = StringVar()
    username = StringVar()
    password = StringVar()

    email.set(setup.EMAIL)
    username.set(setup.CURRENT_USERNAME)

    master_frame_1 = Frame(master=root)
    master_frame_2 = Frame(master=root)
    master_frame_1.pack()
    master_frame_2.pack()

    f1 = Frame(master=master_frame_1)
    f1.pack(side=LEFT)

    label1 = Label(master=f1, text='Email: ', pady=3.5)
    label2 = Label(master=f1, text='Password: ', pady=3.5)
    label3 = Label(master=f1, text='Username: ', pady=3.5)
    label1.pack()
    label2.pack()
    label3.pack()

    f2 = Frame(master=master_frame_1)
    f2.pack()

    # global username, email, password

    entry1 = Entry(master=f2, borderwidth=5, relief=GROOVE, textvariable=email)
    entry2 = Entry(master=f2, borderwidth=5, relief=GROOVE, show='*', textvariable=password)
    entry3 = Entry(master=f2, borderwidth=5, relief=GROOVE, textvariable=username)

    entry1.pack()
    entry2.pack()
    entry3.pack()

    f3 = Frame(master=master_frame_2)
    f3.pack()
    confirm = Button(master=f3, text='Confirm', command=root.close_info)
    confirm.pack()

    root.mainloop()


def save_info():
    global save
    root = Gui()
    label = Label(text='Save login information to be reused next time? ')
    label.pack()

    accept = Button(text='Accept', command=root.save)
    accept.pack(side=LEFT)
    reject = Button(text='Cancel', command=root.dont_save)
    reject.pack()

    root.mainloop()
    record_save(save)


def record_save(option):
    with open('remember-me.txt', 'w') as output_text:
        output_text.write(str(option))


def read_save():
    with open('remember-me.txt', 'r') as input_text:
        return int(input_text.read())


def write_info():
    global email, username
    if setup.EMAIL == email and setup.CURRENT_USERNAME == username:
        pass
    else:
        with open('../resources/remember-me.txt', 'w+') as output_file:
            output_file.write("{},{}".format(email, username))


def read_info():
    with open('../resources/remember-me.txt', 'r') as input_file:
        result = input_file.read()
        result = result.strip().split(",")
    if len(result) == 2:
        setup.EMAIL = result[0]
        setup.CURRENT_USERNAME = result[1]

    else:
        # result = result.strip().split(',')
        setup.EMAIL = ''
        setup.CURRENT_USERNAME = ''


def setup_info():
    setup.EMAIL = email
    setup.PASSWORD = password
    setup.CURRENT_USERNAME = username


def intro_gui():
    intro()
    setup_info()


def details_gui(number_dict=None):
    if number_dict is None:
        number_dict = dict()
    root = Gui()

    account_details = Frame(master=root)
    account_details.pack()
    numbers = Frame(master=root)
    numbers.pack()
    options = Frame(master=root)
    options.pack()

    account_detail_1 = Label(master=account_details, text='Email: {}'.format(setup.EMAIL))
    account_detail_2 = Label(master=account_details, text='Username: {}'.format(setup.CURRENT_USERNAME))
    account_detail_1.pack()
    account_detail_2.pack()

    try:
        posts = Label(master=numbers, text='Posts: {}'.format(number_dict['post']))
        follower = Label(master=numbers, text='Followers: {}'.format(number_dict['follower']))
        following = Label(master=numbers, text='Following: {}'.format(number_dict['following']))
        posts.pack()
        follower.pack()
        following.pack()
    except KeyError:
        pass

    tmp = ''
    for x, y in menu.items():
        tmp += '{} {}\n'.format(x, y)

    option_menu = Label(master=options, text=tmp, justify='left')
    option_menu.pack()

    user_option = StringVar(value='Your option....')
    choice = Entry(master=options, textvariable=user_option)
    choice.pack()

    confirm = Button(master=options, text='Confirm', command=root.destroy)
    confirm.pack()

    root.mainloop()

    return int(user_option.get())


def result_gui():
    pass


def add_status():
    pass


if __name__ == '__main__':
    intro_gui()
    details_gui()
    result_gui()

    pass

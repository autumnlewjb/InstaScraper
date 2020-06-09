from tkinter import *
import Setup
from ctypes import windll

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

    email.set(Setup.EMAIL)
    username.set(Setup.CURRENT_USERNAME)

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
    if Setup.EMAIL == email and Setup.CURRENT_USERNAME == username:
        pass
    else:
        with open('remember-me.txt', 'w+') as output_file:
            output_file.write("{},{}".format(email, username))


def read_info():
    with open('remember-me.txt', 'r') as input_file:
        result = input_file.read()
        result = result.strip().split(",")
    if len(result) == 2:
        Setup.EMAIL = result[0]
        Setup.CURRENT_USERNAME = result[1]

    else:
        # result = result.strip().split(',')
        Setup.EMAIL = ''
        Setup.CURRENT_USERNAME = ''


def setup():
    Setup.EMAIL = email
    Setup.PASSWORD = password
    Setup.CURRENT_USERNAME = username


def gui_implement():
    intro()
    setup()


if __name__ == '__main__':
    gui_implement()

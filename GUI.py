from tkinter import *

email = None
username = None
password = None


class Gui(Tk):
    def close_and_open(self):
        self.destroy()
        get_info()

    def close_and_print(self):
        global email, username, password
        self.destroy()
        email = email.get()
        username = username.get()
        password = password.get()
        print(email, username, password)


def get_info():
    global email, username, password
    root2 = Gui()
    email = StringVar()
    username = StringVar()
    password = StringVar()

    master_frame_1 = Frame(master=root2)
    master_frame_2 = Frame(master=root2)
    master_frame_1.pack()
    master_frame_2.pack()

    f1 = Frame(master=master_frame_1)
    f1.pack(side=LEFT)

    label1 = Label(master=f1, text='Email: ', pady=5)
    label2 = Label(master=f1, text='Password: ', pady=5)
    label3 = Label(master=f1, text='Username: ', pady=5)
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
    confirm = Button(master=f3, text='Confirm', command=root2.destroy)
    confirm.pack()

    root2.mainloop()
    email = email.get()
    username = username.get()
    password = password.get()
    print(email, username, password)


root = Gui()
root.title('Get Started')

label = Label(text='Get Started')
label.pack()

button = Button(text='OK', command=root.close_and_open)
button.pack()
root.mainloop()

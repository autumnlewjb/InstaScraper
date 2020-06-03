from tkinter import *

username = None
email = None
password = None


def get_value(entry1, entry2, entry3):
    global username, email, password



    print(email, password, username)


def get_info():
    root2 = Tk()

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

    entry1 = Entry(master=f2, borderwidth=5, relief=GROOVE)
    entry2 = Entry(master=f2, borderwidth=5, relief=GROOVE, show='*')
    entry3 = Entry(master=f2, borderwidth=5, relief=GROOVE)

    entry1.pack()
    entry2.pack()
    entry3.pack()

    global username, email, password

    f3 = Frame(master=master_frame_2)
    f3.pack()
    confirm = Button(master=f3, text='Confirm', )
    confirm.pack()

    email = entry1.get()
    password = entry2.get()
    username = entry3.get()

    print(username, password, email)

    root2.mainloop()


root = Tk()
root.title('Get Started')

label = Label(text='Get Started')
label.pack()

button = Button(text='OK', command=get_info)
button.pack()

# frame_a = Frame(master=root, width=50, height=50, bg='red')
# frame_a.pack(side=LEFT)
# # label_a = Label(master=frame_a, text='frame 1')
# # label_a.pack()
#
# frame_b = Frame(master=root, bg='blue')
# frame_b.pack(side=LEFT)
# label_b = Label(master=frame_b, text='frame 2')
# label_b.pack()

# main = Frame(root, height=1, width=0.5)
# main.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.1)
# main.pack(anchor=CENTER)
#
# text = Text(main, height=1, width=30)
#
# text.tag_config('center', justify='center')
# text.insert(INSERT, 'Wanna Scrape from Instagram?')
# text.pack(anchor=CENTER)
#
# button = Button(root, text='OK', justify='center')
# button.pack(anchor=S)

root.mainloop()

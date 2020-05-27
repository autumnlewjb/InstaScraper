from tkinter import *

root = Tk()
root.title('Get Started')

main = Frame(root, height=1, width=0.5)
# main.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.1)
main.pack(anchor=CENTER)

text = Text(main, height=1, width=30)

text.tag_config('center', justify='center')
text.insert(INSERT, 'Wanna Scrape from Instagram?')
text.pack(anchor=CENTER)

button = Button(root, text='OK', justify='center')
button.pack(anchor=S)

root.mainloop()

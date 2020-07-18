from abc import abstractmethod, ABCMeta
from ctypes import windll
from tkinter import *


windll.shcore.SetProcessDpiAwareness(1)


class ScraperInterface(metaclass=ABCMeta):

    def result_gui(self):
        tmp = ''
        result = self.main()
        if isinstance(result, list):
            count = 1
            for res in result:
                tmp += '{} {}\n'.format(count, res)
                count += 1

        elif isinstance(result, dict):
            for x, y in result.items():
                print(x, y)
        else:
            tmp = str(result)

        root = Tk()

        text_status = Text(master=root)
        text_status.insert(END, str(tmp))
        text_status.pack()

        confirm = Button(text='OK', command=root.destroy)
        confirm.pack()

        root.mainloop()

    @abstractmethod
    def main(self):
        pass

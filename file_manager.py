from Cleaner import rename_repetition
from setup import SAVE_PATH
import os


class FileManager:

    def __init__(self):
        self.dir = SAVE_PATH
        self.create_folder()

    def create_folder(self):
        exist = os.path.exists(self.dir)
        if not exist:
            os.mkdir(self.dir)
        else:
            pass

    def filename(self):
        name = 'from_insta'
        extension = '.jpeg'
        direct = self.dir + '\\' + name + extension
        tmp = direct
        count = 1
        while os.path.exists(tmp):
            count += 1
            tmp = rename_repetition(direct, count)
            continue

        return tmp


if __name__ == '__main__':
    # new_file = FileManager()
    # print(new_file.filename())

    pass

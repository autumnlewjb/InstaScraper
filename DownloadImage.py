import io
from PIL import Image
from GetImageLink import GetImageLink
import requests
from FileManager import FileManager


class DownloadImage(GetImageLink):

    def __init__(self, browser):
        super().__init__(browser)
        self.byte = self.fetch_image()

    def fetch_image(self):
        complete = []

        req = [requests.get(lk) for lk in self.links]
        in_byte = [io.BytesIO(request.content) for request in req]
        complete.extend(in_byte)

        return complete

    def save_image(self):
        for image in self.byte:
            new_image = Image.open(image)
            new_file = FileManager()
            with open(new_file.filename(), 'wb') as fp:
                new_image.save(fp)
                fp.close()


if __name__ == '__main__':
    pass

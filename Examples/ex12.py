class Phone(object):
    def __init__(self):
        print("Constructing the Phone object...")

    def info(self):
        print("Currently no info available in Phone class")


class Camera(object):
    def take_photo(self):
        print("click click click..")

    def take_photo_with_flash(self):
        print("Lights ON")
        self.take_photo()

    __take_photo = take_photo


class MobilePhone(Phone, Camera):
    def __init__(self):
        super().__init__()
        print("Constructing the MobilePhone object...")

    def take_photo(self):
        super().take_photo()
        print("snap snap...")


if __name__ == "__main__":

    mp = MobilePhone()
    mp.info()
    mp.take_photo_with_flash()

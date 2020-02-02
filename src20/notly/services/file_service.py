from random import seed, randint

class FileService:

    def save_file(self, file):
        file_id = "{}.pdf".format(randint(100000000, 999999999))
        file.save(file_id)
        return file_id
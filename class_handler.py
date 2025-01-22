class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "r")

    def read_data(self):

        return self.file.read()


try:
    file_obj = FileHandler("example1.py")
    print(file_obj.read_data())
except FileNotFoundError:
    print("File doesn't exist")

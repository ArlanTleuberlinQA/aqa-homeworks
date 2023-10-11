from HomeWork12.files.interfaces.iwrite import Write


class TxtWriter(Write):
    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.__text_to_write = "New text in file"

    def write(self):
        with open(self.__file_path, 'w') as file:
            file.write(self.__text_to_write)
            return self.__text_to_write

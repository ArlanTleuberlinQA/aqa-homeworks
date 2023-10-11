from HomeWork12.files.interfaces.iwrite import Write


class TxtWriter(Write):
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def write(self):
        text_to_write = "Newest text"
        with open(self.__file_path, 'w') as file:
            file.write(text_to_write)
            return text_to_write

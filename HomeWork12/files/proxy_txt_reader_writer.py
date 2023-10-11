from HomeWork12.files.interfaces.iread import Read
from interfaces.iwrite import Write
from txt_writer import TxtWriter
from txt_reader import TxtReader


class ProxyTxtRW(Read, Write):

    def __init__(self, real_reader: Read, real_writer: Write):
        self.__result = ''
        self.__is_actual = None
        self.__real_reader = real_reader
        self.__real_writer = real_writer

    def read(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__real_reader.read()
            self.__is_actual = True
            return self.__result

    def write(self):
        if self.__result == self.__real_writer.write():
            return self.__result
        else:
            self.__real_writer.write()
            self.__is_actual = False


if __name__ == '__main__':
    my_writer = TxtWriter('File_name.txt')
    reader_reader = TxtReader('File_name.txt')
    proxy = ProxyTxtRW(reader_reader, my_writer)
    print(proxy.read())
    proxy.write()
    print(proxy.read())

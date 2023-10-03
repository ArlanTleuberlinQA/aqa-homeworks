from HomeWork10.electronic.PC.computer import Laptop


class Storage(Laptop):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model, cpu=None, gpu=None, ram=None, storage=None)
        self.capacity = capacity

    def store_data(self):
        print(f"{self.brand} {self.model} зберігає дані")

    def print_info(self):
        print(f"{self.brand} {self.model} {self.capacity}: {self.capacity} - Накопичувач")


if __name__ == "__main__":
    my_storage = Storage("Seagate", "Firecuda", "2000 Gb")
    my_storage.print_info()
    my_storage.store_data()

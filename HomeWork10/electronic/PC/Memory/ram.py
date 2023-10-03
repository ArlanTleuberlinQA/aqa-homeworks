from HomeWork10.electronic.PC.computer import Laptop


class RAM(Laptop):
    def __init__(self, brand, model, capacity, speed):
        super().__init__(brand, model, cpu=None, gpu=None, ram=None, storage=None)
        self.capacity = capacity
        self.speed = speed

    def store_data(self):
        print(f"{self.brand} {self.model} зберігає дані")

    def print_info(self):
        print(f"{self.brand} {self.model}: {self.capacity} Gb, {self.speed}")


if __name__ == "__main__":
    my_ram = RAM("Corsair", "Vengeance", 16, 200)
    my_ram.print_info()
    my_ram.store_data()

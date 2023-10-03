from HomeWork10.electronic.PC.computer import Laptop
from HomeWork10.electronic.info import Info


class CPU(Laptop, Info):
    def __init__(self, brand, model, cores, clock_speed):
        super().__init__(brand, model, cpu=None, gpu=None, ram=None, storage=None)
        self.cores = cores
        self.clock_speed = clock_speed

    def calculate(self):
        print(f"{self.brand} {self.model} виконує обчислення")

    def print_info(self):
        print(f"{self.brand} {self.model}: {self.cores} ядер, {self.clock_speed} ГГц процесор")


if __name__ == "__main__":
    my_cpu = CPU("AMD", "Ryzen 9 5900HS", 8, 3.3)

    my_cpu.print_info()
    my_cpu.calculate()

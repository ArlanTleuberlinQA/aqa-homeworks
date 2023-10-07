from HomeWork10.electronic.info import HardwareInfo
from HomeWork10.electronic.PC.CPU.cpu import CPU
from HomeWork10.electronic.PC.Videocard.gpu import GPU
from HomeWork10.electronic.PC.Memory.ram import RAM
from HomeWork10.electronic.PC.Memory.storage import Storage


class Laptop(HardwareInfo):
    def __init__(self, brand, model, cpu, gpu, ram, storage):
        super().__init__(brand, model)
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.storage = storage

    def boot_up(self):
        print(f"{self.brand} {self.model} запущено")

    def shut_down(self):
        print(f"{self.brand} {self.model} вимкнено")

    def print_info(self):
        print(f"{self.brand} {self.model} - Модель ноутбука")
        print(f"CPU: {self.cpu.brand} {self.cpu.model} - {self.cpu.cores} ядер, {self.cpu.clock_speed} ГГц")
        print(f"GPU: {self.gpu.brand} {self.gpu.model} - {self.gpu.memory} ГБ пам'яті")
        print(f"RAM: {self.ram.brand} {self.ram.model} - {self.ram.capacity} ГБ, {self.ram.speed} МГц")
        print(f"Storage: {self.storage.brand} {self.storage.model} {self.storage.capacity} Gb")


if __name__ == "__main__":


    gaming_laptop = Laptop(
        brand="ASUS",
        model="ROG Zephyrus G14",
        cpu=CPU("AMD", "Ryzen 9 5900HS", 8, 3.3),
        gpu=GPU("NVIDIA", "GeForce RTX 3060", 6, 1425),
        ram=RAM("Corsair", "Vengeance", 16, 200),
        storage=Storage("Seagate", "Firecuda", 2000))
    gaming_laptop.print_info()
    gaming_laptop.boot_up()
    gaming_laptop.shut_down()

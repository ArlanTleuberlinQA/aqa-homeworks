from HomeWork10.electronic.PC.computer import Laptop


class GPU(Laptop):
    def __init__(self, brand, model, memory, clock_speed):
        super().__init__(brand, model, cpu=None, gpu=None, ram=None, storage=None)
        self.memory = memory
        self.clock_speed = clock_speed

    def render(self):
        print(f"{self.brand} {self.model} відтворює графіку")

    def print_info(self):
        print(f"{self.brand}, {self.model}, {self.memory},{self.clock_speed} Парамерти відеокарти")


if __name__ == "__main__":
    card = GPU("NVIDIA",
               "GeForce RTX 3060",
               "12GB",
               "1320 MHz")
    card.print_info()

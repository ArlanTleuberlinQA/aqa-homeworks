from HomeWork10.electronic.PC.Memory.ram import RAM


class GamingRAM(RAM):
    def __init__(self, brand, model, capacity, speed, rgb_lighting):
        super().__init__(brand, model, capacity, speed)
        self.rgb_lighting = rgb_lighting

    def illuminate(self):
        if self.rgb_lighting:
            print(f"{self.brand} {self.model} освітлюється за допомогою RGB підсвічування")
        else:
            print(f"{self.brand} {self.model} не підсвічується")

    def print_info(self):
        print(f"{self.brand} {self.model} - Геймерська оперативна пам'ять")


if __name__ == "__main__":
    my_g_ram = GamingRAM("Corsair", "Vengeance", 16, 200, True)
    my_g_ram.print_info()
    my_g_ram.illuminate()

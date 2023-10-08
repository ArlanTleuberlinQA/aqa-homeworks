from HomeWork10.electronic.PC.Videocard.gpu import GPU


class GraphicsCard(GPU):
    def __init__(self, brand, model, memory, clock_speed, cooling_type):
        super().__init__(brand, model, memory, clock_speed)
        self.cooling_type = cooling_type

    def cool(self):
        print(f"{self.brand} {self.model} зараз охолоджується за допомогою {self.cooling_type}")

    def print_info(self):
        print(f"{self.brand} {self.model} - Геймерська графічна карта")


if __name__ == "__main__":
    g_card = GraphicsCard("NVIDIA",
                          "GeForce RTX 3060",
                          "12GB",
                          "1320 MHz",
                          "Liquid cooling")
    g_card.cool()
    g_card.print_info()

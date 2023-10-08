from HomeWork10.electronic.PC.CPU.cpu import CPU


class GraphicEngine(CPU):
    def __init__(self, brand, model, cores, clock_speed, graphics_power):
        super().__init__(brand, model, cores, clock_speed)
        self.graphics_power = graphics_power

    def render_graphics(self):
        print(f"{self.brand} {self.model} рендерить графіку з потужністю {self.graphics_power} TFLOPS")

    def print_info(self):
        print(f"{self.brand} {self.model} {self.clock_speed}- Графічний процесор")


if __name__ == "__main__":
    my_gcpu = GraphicEngine("Radeon", "RX Vega 8 iGPU", None, "300 MHz",
                            3.68)
    my_gcpu.render_graphics()
    my_gcpu.print_info()

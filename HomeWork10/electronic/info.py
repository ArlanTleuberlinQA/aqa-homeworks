from abc import ABC, abstractmethod


class Info(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def print_info(self):
        print(f"{self.brand} {self.model}")




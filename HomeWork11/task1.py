class Carriage:
    def __init__(self, number):
        self.number = number
        self.passengers = []

    def add_passenger(self, *passengers):
        for passenger in passengers:
            if len(self.passengers) < 10:
                self.passengers.append(passenger)
            else:
                print(f"Вагон {self.number} вже заповнений!")

    def passengers_list(self):
        return self.passengers

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        return f"[{self.number}]"


class Train:
    def __init__(self, locomotive):
        self.locomotive = locomotive
        self.carriages = []

    def add_carriage(self, *carriage):
        self.carriages.extend(carriage)

    def __len__(self):
        return len(self.carriages)

    def __str__(self):
        carriages_row = "-".join(map(str, self.carriages))
        return f"<={self.locomotive}-{carriages_row}"


if __name__ == "__main__":
    carriage1 = Carriage(1)
    carriage2 = Carriage(2)
    carriage3 = Carriage(3)
    carriage4 = Carriage(4)

    carriage1.add_passenger("Пасажир 1", "Пасажир 1a")
    carriage2.add_passenger("Пасажир 2")
    carriage3.add_passenger("Пасажир 3", "Пасажир 4", "Пасажир 5", "Пасажир 6", "Пасажир 7")
    carriage4.add_passenger(1, 2, 3, 4, 5, 6, 7, 8, 9)
    carriage4.add_passenger(10, 11)

    print(f'Список пасажирів вагона1: {carriage1.passengers_list()}')
    print(f'Список пасажирів вагона2: {carriage2.passengers_list()}')
    print(f'Список пасажирів вагона3: {carriage3.passengers_list()}')
    print(f'Список пасажирів вагона4: {carriage4.passengers_list()}')
    print(f'Кількість пасажирів вагона1: {len(carriage1)}')
    print(f'Кількість пасажирів вагона2: {len(carriage2)}')
    print(f'Кількість пасажирів вагона3: {len(carriage3)}')
    print(f'Кількість пасажирів вагона4: {len(carriage4)}')
    print(f'Номера вагонів з голови поїзда: {carriage1}, {carriage2}, {carriage3}, {carriage4}')

    train = Train("[HEAD]")
    train.add_carriage(carriage1, carriage2, carriage3, carriage4)
    print(f'Кількість вагонгів: {len(train)}')
    print(train)

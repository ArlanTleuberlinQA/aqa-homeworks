class Worker:
    __address = "м. Київ, вулиця Жилянська, 42, кв. 10"
    """
   Клас, що описує робітника
    Атрибути:
        name (str): Ім'я робітника.
        employee_id (int): Унікальний ідентифікатор робітника.
        position (str): Посада  робітника.
        salary (float): Заробітна плата робітника у доларах США.
    """

    def __init__(self, name: str, employee_id: int, position: str, salary: float):
        """
        Ініціалізація об'єкту класу Worker.


        """
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.salary = salary


    def calculate_yearly_income(self) -> float:
        """
        Обчислює щорічний дохід робітника на основі щомісячної заробітної плати.

        """
        return self.salary * 12

    def promote(self, new_position: str):
        """
        Змінює посаду робітника

        """
        self.position = new_position

    def display_info(self):
        """
        Показує інформацію про робітника.

        Returns:
            str: Рядок, що містить ім'я робітника, ідентифікатор працівника, посаду і заробітну плату.
        """
        info = f"Ім'я: {self.name}\nІдентифікатор працівника: {self.employee_id}\nПосада: {self.position}\nЗарплата: {self.salary}$"
        return info

    @staticmethod
    def get_address():
        """
        Повертає адресу робітника.

        Returns:
            str: Адреса робітника.
        """
        return Worker.__address

    @classmethod
    def set_address(cls, new_address: str):
        """
        Встановлює нову адресу .

        Args:
            new_address (str): Нова адреса.
        """
        cls.__address = new_address


if __name__ == "__main__":
    worker1 = Worker("Іван Петров", 1, "Менеджер", 5000.0)
    print(worker1.display_info())

    print(f'Стара адреса: {Worker.get_address()}')

    Worker.set_address("м. Львів, вулиця Галицька, 24, кв. 5")
    print(f'Нова адреса:{Worker.get_address()}')
    worker1.promote("CTO")
    print(worker1.display_info())
    print(f'Зарплата за рік: {worker1.calculate_yearly_income()}$')


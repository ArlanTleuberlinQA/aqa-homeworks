class Company:
    """
    Клас, що описує компанію.

    Attributes:
        name: Назва компанії.
        founding_year: Рік заснування компанії.
        headquarters: Місто розташування головного офісу.
        industry: Галузь, в якій діє компанія.
        revenue: Річний дохід компанії в мільярдах доларів.
        founder (str): Ім'я засновника компанії.
        ceo (str): Ім'я поточного виконавчого директора компанії.
    """

    def __init__(self, name, founding_year, headquarters, industry, revenue, ceo, founder):
        """
        Ініціалізація об'єкту компанії з вказаними атрибутами.

        """
        self.name = name
        self.founding_year = founding_year
        self.headquarters = headquarters
        self.industry = industry
        self.__revenue = revenue
        self.founder = founder
        self.ceo = ceo

    def get_revenue(self):
        """
        Гетер для отримання річного доходу компанії.


        """
        return self.__revenue

    def set_revenue(self, revenue):
        """
        Сетер для встановлення річного доходу компанії.


        revenue:  Новий річний дохід компанії в мільярдах доларів.
        """
        if revenue >= 0:
            self.__revenue = revenue
        else:
            print("Помилка: Річний дохід повинен бути не менше 0.")

    @staticmethod
    def get_age(current_year, founding_year):
        """
        Статичний метод для обчислення віку компанії на певну дату.

        """
        age = current_year - founding_year
        return age

    @classmethod
    def create_company(cls, name, founding_year, headquarters, industry, revenue):
        """
        Класовий метод для того, щоб передати всі данні компанії в одну змінну.

        """
        return cls(name, founding_year, headquarters, industry, revenue)

    def __str__(self):
        """
        Метод для представлення об'єкту компанії у вигляді рядка.

        Returns:
            str: Рядок, що містить інформацію про компанію
        """
        return f"{self.name} ({self.founding_year}), {self.industry}, HQ: {self.headquarters}\n" \
               f"Засновник: {self.founder}\n" \
               f"CEO: {self.ceo}"


if __name__ == "__main__":
    apple = Company("Apple Inc.", 1976, "Cupertino, California", "Технології", 394.46, "Tim Cook", "Steve Jobs")
    print(apple)
    print(f"Вік компанії: {Company.get_age(2023, apple.founding_year)} роки")
    print(f"Річний дохід: {apple.get_revenue()} мільярда доларів")
    # Змінюємо значення річного доходу компанії
    apple.set_revenue(400)
    print(f"Новий річний дохід: {apple.get_revenue()} мільярда доларів")

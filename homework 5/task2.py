class FormulaError(Exception):
    pass


class WrongOperatorError(Exception):
    pass


attempts = 3
for attempt in range(1, attempts + 1):
    try:
        formula = input("Введіть вираз (наприклад, 2 * 5): ")
        elements = formula.split()

        if len(elements) != 3:
            raise FormulaError("Формула має складатися з трьох елементів.")
        num1 = float(elements[0])
        operator = elements[1]
        num2 = float(elements[2])

        if operator not in ('*', '/'):
            raise WrongOperatorError("Допускаються лише операції множення (*) або ділення (/).")

        if operator == '/' and num2 == 0:
            raise ZeroDivisionError("Ділення на нуль недопустимо.")

        if operator == '*':
            result = num1 * num2
        else:
            result = num1 / num2

    except (WrongOperatorError, FormulaError, ZeroDivisionError) as e:
        print(f"Помилка: {e}")
    except ValueError as e:
        try:
            raise ValueError("Введені дані не є числами.")
        except ValueError as custom_error:
            print(f"Помилка в значенні: {custom_error}")
    else:
        print(f"Результат: {result:.2f}")
        break
    finally:
        print(f"Спроба {attempt} з {attempts}")

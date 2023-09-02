# task 1

c = int((input("Введіть температуру за Цельсієм ")))
f = float(c * 9 / 5 + 32)  # в умовах задачі помилка, 25 градусів за Цельсієм це 77 за Фаренгейтом
k = c + 273.15
print("Фаренгейт:", f)
print("Кельвін:", k)
print("=" * 20)

# task 2

v1 = int((input("Вкажіть об'єм першої ємності ")))
v2 = int((input("Вкажіть об'єм другої ємності ")))
t1 = int((input("Вкажіть температуру першої ємності ")))
t2 = int((input("Вкажіть температуру другої ємності ")))
v3 = int(v1 + v2)
print("Об'єм:", (int(v3)))
t3 = float((v1 * t1 + v2 * t2) / (v1 + v2))
print("Температура:", float(t3))
print("=" * 20)

# task 3

calc_1 = int(input("Перше число "))
calc_2 = int(input("Друге число "))
calc_3 = input("Що робимо? ")
a = calc_1
b = calc_2
if calc_3 == "+":
    print(a + b)
if calc_3 == "-":
    print(a - b)
if calc_3 == "*":
    print(a * b)
if b == 0 and calc_3 == "/":
    print("Ділення на 0")
elif calc_3 == "/":
    print(a / b)
else:
    print("Введіть правильний символ")

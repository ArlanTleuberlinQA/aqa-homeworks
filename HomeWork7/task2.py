

def square(arg):
    p = arg * 4
    s = arg ** 2
    d = (2**0.5) * arg
    print(f'Периметр: {p},Площа: {s},Діагональ: {d}')


sight = int(input("Введіть довжину сторони квадрата: "))
if __name__ == '__main__':
    square(sight)

def display_box(width: int, height: int, character="*"):
    print(width * character)
    for i in range(height):
        if i % 2 == 0:
            print(character + ' ' * (width - 2) + character)
    print(width * character)


for_user = input("Введіть довжину, висоту та за бажанням символ: ")
elements = for_user.split()
width_1 = int(elements[0])
height_1 = int(elements[1])
len_inp = for_user.split()
if __name__ == '__main__':
    if len(len_inp) == 3:
        character_1 = elements[2]
        display_box(width_1, height_1, character_1)
    else:
        display_box(width_1, height_1)



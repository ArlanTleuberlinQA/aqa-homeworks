def display_box(width: int, height: int, character="*"):
    print(width * character)
    for i in range(height):
        if i % 2 == 0:
            print(character + ' '*(width-2) + character)
    print(width * character)


for_user = input("Введіть довжину, висоту та символ: ")
elements = for_user.split()
width = int(elements[0])
height = int(elements[1])
char = str(elements[2])
if __name__ == '__main__':
    display_box(width, height, char)

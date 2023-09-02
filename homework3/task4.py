text = input(str("Введіть текст: "))
my_list = text.split()
l_check = len(my_list)
if l_check > 3:
   print(my_list[-3:])
else:
    print(str("Кількість елементів:"), int(l_check))
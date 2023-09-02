ip_adr = input("Введіть айпі адресу: ")
ip_list = ip_adr.split(".")
count_check = len(ip_list)
for item in ip_list:
    if item.isdigit() is False:
        print("Неправильна IP-адреса")
        break
    if count_check != 4:
        print("Неправильна IP-адреса1")
    elif ip_adr.count(".") != 3:
        print("Неправильна IP-адреса2")
    if int(item) > 255:
        print("Неправильна IP-адреса3")
        break


palindrome = input(str("Введіть слово "))
if palindrome == palindrome[::-1]:
    print("+")
else:
    print("-")


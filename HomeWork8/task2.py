def my_gen(a):
    for num in range(a):
        if num % 2 == 0:
            yield num ** 2


gen = my_gen(1000000001)

for num_1 in gen:
    print(num_1)

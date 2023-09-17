names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
for i in names:
    if not isinstance(i, str):
        continue
    else:
        print(i)

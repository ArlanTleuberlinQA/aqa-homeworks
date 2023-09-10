import os

file_sizes = {}
largest_file_size = 0
for root, dirs, files in os.walk('./..'):
    for filename in files:
        file_path = os.path.join(root, filename)
        size = os.path.getsize(file_path)
        file_sizes[filename] = size
        sort = str(file_sizes)
        if size > largest_file_size:
            largest_file_size = size
            largest_file = filename
with open('files_size.txt', 'w') as f:
    for filename, size in file_sizes.items():
        f.write(f"{filename}: {size: } B\n")

    print(f"Найбільший файл: {largest_file}, Розмір: {largest_file_size: } B")


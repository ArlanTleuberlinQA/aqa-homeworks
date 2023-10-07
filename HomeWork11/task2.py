class CustomIterator:
    def __init__(self, sequence, start_index, end_index):
        self.sequence = sequence
        self.start_index = start_index
        self.end_index = end_index
        self.current_index = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.start_index or self.current_index > self.end_index:
            raise StopIteration
        else:
            value = self.sequence[self.current_index]
            self.current_index += 1
            return value


my_sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
iterator = CustomIterator(my_sequence, 2, 7)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


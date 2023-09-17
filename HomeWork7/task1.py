def sum_range(start, end):
    ranger = range(start, end+1)
    if end < start:
        ranger = range(end, start+1)
        return sum(ranger)
    else:
        return sum(ranger)


sum_num = input("Введіть числа у порядку зростання: ")
sum_split = sum_num.split()
sum_start = int(sum_split[0])
sum_end = int(sum_split[-1])
if __name__ == '__main__':
    print(sum_range(sum_start, sum_end))

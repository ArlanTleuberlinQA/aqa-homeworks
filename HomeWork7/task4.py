def my_map(func, a):
    result = []
    for i in a:
        result.append(func(i))
    return result



str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
int_list = list(my_map(int, str_list))
step_list = list(my_map(lambda x: x ** 2, int_list))
final_dict = dict(zip(int_list, step_list))
if __name__ == '__main__':
    print(final_dict)

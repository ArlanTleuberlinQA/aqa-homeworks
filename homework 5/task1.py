str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
int_list = list(map(int, str_list))
step_list = list(map(lambda x: x**2,int_list))
final_dict = dict(zip(int_list,step_list))
print(final_dict)
CamelCase = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = [''.join(['_' + i.lower() if i.isupper() else i for i in word]).lstrip('_') for word in CamelCase]
print(snake_case_list)


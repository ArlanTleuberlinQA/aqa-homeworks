lang_dict = {'Python':'Guido van Rossum','Java':' James Gosling','JavaScript':'Brendan Eich','C++':'Bjarne Stroustrup'}
for language, developer in lang_dict.items():
    answer = f"My favorite programming language in {language}.It was created by {developer}"
    print(answer)
lang_dict.pop("C++")
print(lang_dict)

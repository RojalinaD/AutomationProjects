# Sorting a list of dictionaries using sorted() and itemgetter()

from operator import itemgetter

list1 = [{"name": "Nandini", "age": 20},
        {"name": "Manjeet", "age": 20},
        {"name": "Nikhil", "age": 19}]

sorted_list1 = sorted(list1, key=itemgetter('age'))
print(sorted_list1)

sorted_list2 = sorted(list1, key=itemgetter('name','age'))
print(sorted_list2)

sorted_list3 = sorted(list1, key=itemgetter('age'), reverse=True)
print(sorted_list3)



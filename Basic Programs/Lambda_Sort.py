# Sorting a list of dictionaries using lambda()

list1 = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

#sorted_list1 = sorted(list1, key=lambda i:i['age'])
#print(sorted_list1)

#sorted_list2 = sorted(list1, key=lambda i:i['name'], reverse=True)
#print(sorted_list2)

sorted_list3 = sorted(list1, key=lambda i:(i['age'],i['name']))
print(sorted_list3)

sorted_list4 = sorted(list1, key=lambda i:i['name'], reverse=True)
print(sorted_list4)

sorted_list5 = sorted(list1, key=lambda i:(i['age'],i['name']), reverse=True)
print(sorted_list5)




#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    for i in range(len(my_list)):
        if (i != idx):
            new_list.append(my_list[i])
    my_list = new_list
    return my_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)



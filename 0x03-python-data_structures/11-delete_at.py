#!/usr/bin/python3
def replace_in_list(my_list, idx=0):
    tmp = []
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    for i in my_list:
        if i != my_list[idx]:
            tmp.append(i)
    my_list = tmp
    return (my_list)

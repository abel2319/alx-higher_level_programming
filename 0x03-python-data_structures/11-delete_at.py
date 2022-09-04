#!/usr/bin/python3
def replace_in_list(my_list, idx=0):
    tmp = []
    if idx >= 0 or idx < len(my_list):
        del my_list[idx]
    return (my_list)

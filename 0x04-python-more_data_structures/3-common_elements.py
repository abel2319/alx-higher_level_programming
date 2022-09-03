#!/usr/bin/python3
def common_elements(set_1, set_2):
    size = len(set_1) if len(set_1) < len(set_2) else len(set_2)
    new_list = []
    for i in range(size):
        if set_1[i] == set_2[i]:
            new_list.append(set_1[i])
    return (new_list)

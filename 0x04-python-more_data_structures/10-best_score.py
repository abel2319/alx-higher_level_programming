#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    if new_dict != {}:
        key_list = list(new_dict.keys())
        j = key_list[0]
        for i in new_dict.keys():
            if new_dict[i] >= new_dict[j]:
                j = i
        return (j)
    return (None)

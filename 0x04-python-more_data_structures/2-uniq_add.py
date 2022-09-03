#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    rtn = 0
    if my_list != []:
        new_list = [i for i in my_list]
        new_list.sort()
        rtn = new_list[0]
        for i in range(1, len(new_list)):
            if new_list[i] != new_list[i - 1]:
                rtn += new_list[i]
    return (rtn)

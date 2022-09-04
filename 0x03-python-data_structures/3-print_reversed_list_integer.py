#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    nbr = len(my_list)
    for i in range(nbr):
        print('{:d}'.format(my_list[nbr - (i + 1)]))

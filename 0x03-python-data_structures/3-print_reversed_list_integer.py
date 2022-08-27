#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    nbr = len(my_list)
    for i in range(nbr):
        print('{}'.format(my_list[nbr - i]))

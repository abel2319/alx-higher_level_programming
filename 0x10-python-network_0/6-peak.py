#/usr/bin/python3
"""Module that defines the function find_peak"""


def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers.
    Args:
        lis_of_integers (list): the list
    """
    if list_of_integers is not None and len(list_of_integers) != 0:
        list_of_integers.sort()
        return (list_of_integers[-1])
    return (None)

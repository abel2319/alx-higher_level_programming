#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    if new_dict != {}:
        best_score = None
        j = 0
        for i in new_dict():
            if new_dict[i] >= j:
                j = i
                best_score = i
        return (best_score)
    return (None)

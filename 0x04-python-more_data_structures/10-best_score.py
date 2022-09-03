#!/usr/bin/python3
def best_score(a_dictionary):

    best_score = None

    if a_dictionary is not None:
        j = 0
        for i in a_dictionary:
            if a_dictionary[i] > j:
                j = a_dictionary[i]
                best_score = i

    return (best_score)

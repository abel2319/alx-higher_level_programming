#!/usr/bin/python3
def remove_char_at(str, n):
    j = 0
    tmp = ""
    if str != "":
        for i in str:
            if (j != n):
                tmp += i
            j = j + 1
    return (tmp)

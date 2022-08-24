#!/usr/bin/python3
def uppercase(str):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in len(str):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            str[i] = alpha[ord(str[i]) - 97]
    print("{}".format(str))

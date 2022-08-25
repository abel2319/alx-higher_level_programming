#!/usr/bin/python3
def uppercase(str):
    j = 0
    alpha = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            alpha += "%c" % (ord(i) - 32)
        else:
            alpha += "%c" % (ord(i))
    print("{}".format(alpha))

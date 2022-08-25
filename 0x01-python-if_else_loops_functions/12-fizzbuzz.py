#!/usr/bin/python3
def fizzbuzz():
    print("1 2 ", end="")
    for i in range(3, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print("fizzbuzz ", end="")
        elif (i % 3 == 0):
            print("fizz ", end="")
        elif (i % 5 == 0):
            print("buzz ", end="")
        else:
            print("{:d} ".format(i), end="")

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    j = 0
    for i in argv[1:]:
        j += int(i)
    print("{:d}".format(j))

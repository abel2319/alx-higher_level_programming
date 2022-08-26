#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nbr = len(sys.argv)
    j = 1
    if (nbr > 1):
        if nbr == 2:
            print("1 argument:\n1: {}".format(sys.argv[1]))
        else:
            print("{:d} arguments:".format(nbr - 1))
            for i in range(1, nbr):
                print("{}: {}".format(j, sys.argv[i]))
                j += 1
    if (nbr <= 1):
        print("0 arguments.")

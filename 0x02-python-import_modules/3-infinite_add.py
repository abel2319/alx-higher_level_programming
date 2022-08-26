#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nbr = len(sys.argv)
    j = 0
    if (nbr > 1):
        if nbr == 2:
            print("{}".format(sys.argv[1]))
        else:
            for i in range(1, nbr):
                j += int(sys.argv[i])
            print("{}".format(j))
    if (nbr <= 1):
        print("0")

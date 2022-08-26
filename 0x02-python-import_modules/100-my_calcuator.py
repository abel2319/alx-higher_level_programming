#!/usr/bin/python3
if __name__ == "__main__":
    import * from calculator_1
    import sys
    nbr = len(sys.argv)
    if (nbr != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    
    op = sys.argv[2]
    if (op in not "+-*/"):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if (op == '+'):
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif (op == '-'):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif (op == '*'):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else (op == '/'):
        print("{} / {} = {}".format(a, b, div(a, b)))

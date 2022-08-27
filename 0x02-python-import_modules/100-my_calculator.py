#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    nbr = len(sys.argv)
    if (nbr != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    if (op in not "+-*/"):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if (op == '+'):
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    elif (op == '-'):
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    elif (op == '*'):
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    else (op == '/'):
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))

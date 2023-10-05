#!/usr/bin/python3

import operator
import sys

if __name__ == "__main__":
    """Handle basic arithmetic operations."""

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

    if sys.argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
    except ValueError:
        print("Invalid input. Please provide valid integer values for <a> and <b>")
        sys.exit(1)

    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))

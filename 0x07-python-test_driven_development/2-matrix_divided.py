#!/usr/bin/python3
'''this module allows the division of all elts in a matrix'''


def matrix_divided(matrix, div):
    '''This fucntion divides all elts in matrix
       args:
            matrix (list): the matrix
            div (int/float): the divisor
       Exceptions:
            TypeError
            ZeroDivisionError
       Return: new matrix containing the elts divided
    '''
    tmp_matrix = []

    if (type(div) is not int) and (type(div) is not float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    d = len(matrix[0])
    for i in matrix:
        if (type(i) is not list):
            raise TypeError("matrix must be a matrix (list of lists) +"
                            "of integers/floats")
        else:
            if len(i) != d:
                raise TypeError("Each row of the matrix " +
                                "must have the same size")
            for j in i:
                if (type(j) is not int) and (type(j) is not float):
                    raise TypeError("matrix must be a matrix (list of lists) +"
                                    "of integers/floats")

    for i in matrix:
        tmp_matrix.append([round((j / div), 2) for j in i])
    return tmp_matrix

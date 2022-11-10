"""
Thomas Kanenaga
CSE 163 AD

This file contains three functions that solve 3 problems out of HW0.
"""


def funky_sum(a, b, mix):
    """
    This function takes in the parameters of  two numbers and
    a third opperator number finds the number to return based
    on the opporators number.
    """
    if mix <= 0:
        return a
    elif mix >= 1:
        return b
    elif mix > 0 and mix < 1:
        return (1 - mix) * a + mix * b


def total(n):
    """
    This function takes the parameter "n" and finds sum of
    the numbers from zero to n including both.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def swip_swap(source, c1, c2):
    """
    This function takes in the parameters of a string
    and two characters then switches all instances of
    each characters returning the string with the two
    instwances switched.
    """
    for letter in range(len(source)):
        if source[letter] == c2:
            source = source[:letter] + c1 + source[letter + 1:]
        elif source[letter] == c1:
            source = source[:letter] + c2 + source[letter + 1:]
    return source

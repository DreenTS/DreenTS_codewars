"""
LINK = https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b/

The purpose of this kata is to write a program that can do some algebra.

Write a function expand that takes in an expression with a single, one character variable, and expands it.
The expression is in the form (ax+b)^n where a and b are integers which may be positive or negative,
x is any single character variable, and n is a natural number. If a = 1, no coefficient will be placed in front of the
variable. If a = -1, a "-" will be placed in front of the variable.

The expanded form should be returned as a string in the form ax^b+cx^d+ex^f... where a, c, and e are the coefficients
of the term, x is the original one character variable that was passed in the original expression and b, d, and f,
are the powers that x is being raised to in each term and are in decreasing order.

If the coefficient of a term is zero, the term should not be included. If the coefficient of a term is one,
the coefficient should not be included. If the coefficient of a term is -1, only the "-" should be included.
If the power of the term is 0, only the coefficient should be included. If the power of the term is 1,
the caret and power should be excluded.

Examples:
expand("(x+1)^2")      # returns "x^2+2x+1"
expand("(p-1)^3")      # returns "p^3-3p^2+3p-1"
expand("(2f+4)^6")     # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
expand("(-2a-4)^0")    # returns "1"
expand("(-12t+43)^2")  # returns "144t^2-1032t+1849"
expand("(r+0)^203")    # returns "r^203"
expand("(-x-1)^2")     # returns "x^2+2x+1"
"""


from math import factorial
import re


POWER_RE = re.compile(r'\^\d+')
SYMB_RE = re.compile(r'-?\w+')
OPERATOR_RE = re.compile(r'[a-zA-Z]+[+-]+')
Y_RE = re.compile(r'\d+\)')


def expand(expr):
    power = int(re.search(POWER_RE, expr).group()[1:])
    if power == 0:
        return '1'
    symb = re.search(SYMB_RE, expr).group()
    if len(symb) == 1:
        coeff = 1
    elif len(symb) == 2:
        coeff = -1 if expr[1] == '-' else int(symb[:-1])
    else:
        coeff = int(symb[:-1])
    symb = symb[-1]
    operator = re.search(OPERATOR_RE, expr).group()[-1]
    negative_coeff = -1 if operator == '-' else 1
    y = int(re.search(Y_RE, expr).group()[:-1])
    n = power
    const_n = factorial(power)
    result_string = ''
    for k in range(power + 1):
        c = const_n // (factorial(k) * factorial(power - k))
        curr_coeff = coeff ** n
        curr_member = c * curr_coeff * (y ** k) * (negative_coeff ** k)
        result_string += f"{'+' if curr_member > 0 else ''}"
        if n >= 1:
            if curr_member != 1:
                result_string += f"{curr_member}"
            result_string += f"{symb}^{n}" if n > 1 else symb
        else:
            result_string += f"{curr_member}"
        n -= 1
        k += 1
    return result_string[1:] if result_string[0] == '+' else result_string


if __name__ == '__main__':
    assert expand("(x+1)^0") == "1"
    assert expand("(x+1)^1") == "x+1"
    assert expand("(x+1)^2") == "x^2+2x+1"
    assert expand("(x-1)^0") == "1"
    assert expand("(x-1)^1") == "x-1"
    assert expand("(x-1)^2") == "x^2-2x+1"
    assert expand("(5m+3)^4") == "625m^4+1500m^3+1350m^2+540m+81"
    assert expand("(2x-3)^3") == "8x^3-36x^2+54x-27"
    assert expand("(7x-7)^0") == "1"
    assert expand("(-5m+3)^4") == "625m^4-1500m^3+1350m^2-540m+81"
    assert expand("(-2k-3)^3") == "-8k^3-36k^2-54k-27"
    assert expand("(-7x-7)^0") == "1"

"""
Interweave the Inequalities and the Integers
LINK: https://www.codewars.com/kata/624dfbc87ee0d200157ad483/

In this kata you will be given:

A string of n inequality symbols; i.e. > or <
n+1 distinct integers.
Your goal is to place all of the n+1 integers into the available positions created by the given n inequality symbols,
so that the entire resulting expression is True.

Just to be clear, if you have n inequality symbols there are n-1 positions "inside" the string where you can place n-1
distinct integers, and then there are 2 more positions "outside" the string - one at the beginning, and one other
at the end - where you can place 2 more integers. This is why you will always be given n inequality symbols and
n+1 distinct integers.

_ < _ > _ > _ < _ < _ > _ < _ > _

So, in the illustration above we have n = 8 inequality symbols, and n+1 = 9 empty positions, represented by _,
in which to place the n+1 = 9 integers.

Inputs
ineqs = a string of n inequality symbols with no spaces, e.g. '<><<><><'
ints = a tuple/vector (depending on language) of n+1 distinct integers, e.g. (12, 9, 31, 47, 15, 11, 22, 8, 4)
Performance requirements: Values up to n = 10000 will be used in the random tests.

Output
You will return an array of the n+1 integers, in the order in which you want to insert them into the
n+1 inequality positions.

The tests will then insert the elements of your solution into the inequalities and check that the resulting
expression evaluates to True.

The tests will also check that you have used all the integers from the input.

Example, with n = 8 inequalities and n+1 = 9 integers
ineqs = '<><<><><'

ints = (12, 9, 31, 47, 15, 11, 22, 8, 4)
For these inputs, a valid solution for you to return is - for example - the array:

[8, 31, 4, 9, 47, 12, 22, 11, 15]
because the resulting Boolean expression:

8 < 31 > 4 < 9 < 47 > 12 < 22 > 11 < 15
will indeed evaluate to True.
"""


def interweave(ineqs, ints):
    sorted_ints = sorted(ints)
    result_list = []
    for i in ineqs:
        if i == '<':
            result_list.append(sorted_ints[0])
        else:
            result_list.append(sorted_ints[-1])
        sorted_ints.remove(result_list[-1])
    result_list.append(sorted_ints[0])
    return result_list


if __name__ == '__main__':
    assert interweave('<<<<<', (5, 3, 2, 4, 1, 6)) == [1, 2, 3, 4, 5, 6]
    assert interweave('>', (1, 10000)) == [10000, 1]
    assert interweave('><><><<<<<>><<<><<><<><><><>><<<<><',
                      (9898, 5502, 2002, 895, 9667, 7255, 4699, 4640, 4978, 3901, 2057, 9772, 4643, 466, 4871, 6329,
                       9045, 333, 7598, 8944, 749, 6514, 7697, 9025, 2520, 175, 8248, 4644, 4100, 8009, 6212, 258, 7196,
                       671, 1761, 1703)) == [9898, 175, 9772, 258, 9667, 333, 466, 671, 749, 895, 9045, 9025, 1703,
                                             1761, 2002, 8944, 2057, 2520, 8248, 3901, 4100, 8009, 4640, 7697, 4643,
                                             7598, 4644, 7255, 7196, 4699, 4871, 4978, 5502, 6514, 6212, 6329]

"""
Bananas
LINK: https://www.codewars.com/kata/5917fbed9f4056205a00001e/

Given a string of letters a, b, n how many different ways can you make the word "banana" by crossing out
various letters and then reading left-to-right?

(Use - to indicate a crossed-out letter)

Example
Input

bbananana
Output

b-anana--
b-anan--a
b-ana--na
b-an--ana
b-a--nana
b---anana
-banana--
-banan--a
-bana--na
-ban--ana
-ba--nana
-b--anana
Notes
You must return all possible bananas, but the order does not matter
The example output above is formatted for readability. Please refer to the example
tests for expected format of your result.
:-)
"""

import itertools


def bananas(input_str):
    result = set()
    str_indexes = [i for i, s in enumerate(input_str)]
    combs = itertools.combinations(str_indexes, len('banana'))
    for c in combs:
        temp_str = [input_str[i] for i in c]
        if ''.join(temp_str) == 'banana':
            for i in range(len(input_str)):
                if i not in c:
                    temp_str.insert(i, '-')
            result.add(''.join(temp_str))
    return result


if __name__ == '__main__':
    assert bananas(input_str='bbananana') == {'b-anana--',
                                              'b-anan--a',
                                              'b-ana--na',
                                              'b-an--ana',
                                              'b-a--nana',
                                              'b---anana',
                                              '-banana--',
                                              '-banan--a',
                                              '-bana--na',
                                              '-ban--ana',
                                              '-ba--nana',
                                              '-b--anana'}

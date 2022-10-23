"""
LINK: https://www.codewars.com/kata/58f9f9f58b33d1b9cf00019d/

Given a list of prime factors, primesL, and an integer, limit, try to generate in order, all the numbers less than
the value of limit, that have all and only the prime factors of primesL

Example
primesL = [2, 5, 7]
limit = 500
List of Numbers Under 500          Prime Factorization
___________________________________________________________
           70                         [2, 5, 7]
          140                         [2, 2, 5, 7]
          280                         [2, 2, 2, 5, 7]
          350                         [2, 5, 5, 7]
          490                         [2, 5, 7, 7]
There are 5 of these numbers under 500 and the largest one is 490.

Task
For this kata you have to create the function count_find_num(), that accepts two arguments: primesL and limit,
and returns the amount of numbers that fulfill the requirements, and the largest number under limit.

The example given above will be:

primesL = [2, 5, 7]
limit = 500
count_find_num(primesL, val) == [5, 490]
If no numbers can be generated under limit then return an empty list:

primesL = [2, 3, 47]
limit = 200
find_nums(primesL, limit) == []
The result should consider the limit as inclusive:

primesL = [2, 3, 47]
limit = 282
find_nums(primesL, limit) == [1, 282]
Features of the random tests:

number of tests = 200
2 <= length_primesL <= 6 // length of the given prime factors array
5000 <= limit <= 1e17
2 <= prime <= 499  // for every prime in primesL
Enjoy!
"""

import math
import itertools


def count_find_num(primesL, limit):
    dict_for_combs = {}
    for p in primesL:
        log_limit = math.floor(math.log(limit, p))
        dict_for_combs[p] = [x for x in range(1, log_limit + 1)]
    combinations = itertools.product(*dict_for_combs.values())
    res_set = set()
    for comb in combinations:
        num = 1
        for i in range(len(primesL)):
            num *= primesL[i] ** comb[i]
        if num <= limit:
            res_set.add(num)
    if res_set:
        return [len(res_set), max(res_set)]
    else:
        return []


if __name__ == '__main__':
    assert count_find_num(primesL=[2, 3, 47], limit=282) == [1, 282]

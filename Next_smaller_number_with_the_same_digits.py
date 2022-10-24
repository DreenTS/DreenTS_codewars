"""
Next smaller number with the same digits
LINK: https://www.codewars.com/kata/5659c6d896bc135c4c00021e/

Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains
the same digits. Also return -1 when the next smaller number with the same digits would require
the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
some tests will include very large numbers.
test data only employs positive integers.
The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."
"""


import re


def next_smaller(num):
    if len(set(str(num))) == 1:
        return -1
    num_wo_zeros = re.sub(r'0', '', str(num))
    first_symb = min(num_wo_zeros)
    sorted_num = sorted(str(num))
    sorted_num.remove(first_symb)
    min_num = int(first_symb + ''.join(sorted_num))
    if min_num == num:
        return -1
    digits = list(str(num))
    for i in range(len(digits) - 1, -1, -1):
        end_of_num = digits[i:]
        if digits[i] > min(end_of_num):
            max_from_end = max([(j, end_of_num[j]) for j in range(len(end_of_num)) if end_of_num[j] < digits[i]])
            end_of_num.pop(max_from_end[0])
            digits[i:] = [max_from_end[1]] + sorted(end_of_num, reverse=True)
            return int(''.join(digits))
    return -1


if __name__ == '__main__':
    assert next_smaller(907) == 790
    assert next_smaller(531) == 513
    assert next_smaller(135) == -1
    assert next_smaller(2071) == 2017
    assert next_smaller(414) == 144
    assert next_smaller(123456798) == 123456789
    assert next_smaller(123456789) == -1
    assert next_smaller(1234567908) == 1234567890

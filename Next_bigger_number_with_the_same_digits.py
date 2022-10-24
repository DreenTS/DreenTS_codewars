"""
Next bigger number with the same digits
LINK: https://www.codewars.com/kata/55983863da40caa2c900004e/

Create a function that takes a positive integer and returns the next bigger number that
can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1:

9 ==> -1
111 ==> -1
531 ==> -1
"""


def next_bigger(num):
    if len(set(str(num))) == 1:
        return -1
    temp = num
    max_num = int(''.join(sorted(str(num), reverse=True)))
    while temp < max_num:
        temp += 1
        if sorted(str(temp)) == sorted(str(num)):
            return temp
    return -1


if __name__ == '__main__':
    assert next_bigger(12) == 21
    assert next_bigger(513) == 531
    assert next_bigger(2017) == 2071
    assert next_bigger(414) == 441
    assert next_bigger(144) == 414

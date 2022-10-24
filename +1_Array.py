"""
LINK: https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/

Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.

Examples
[4, 3, 2, 5] would return [4, 3, 2, 6]
[1, 2, 3, 9] would return [1, 2, 4, 0]
[9, 9, 9, 9] would return [1, 0, 0, 0, 0]
[0, 1, 3, 7] would return [0, 1, 3, 8]
"""


def up_array(arr):
    str_array = ''.join([str(a) for a in arr])
    try:
        str_to_int = int(str_array)
        if str_to_int < 0 or len(str_array) != len(arr):
            return None
        new_str = str(str_to_int + 1)
        new_array = list('0' * (len(arr) - len(new_str)) + new_str)
        return [int(i) for i in new_array]
    except ValueError:
        return None


if __name__ == '__main__':
    assert up_array([2, 3, 9]) == [2, 4, 0]
    assert up_array([4, 3, 2, 5]) == [4, 3, 2, 6]
    assert up_array([1, -9]) is None
    assert up_array([9, 9]) == [1, 0, 0]
    assert up_array([0, 4, 2]) == [0, 4, 3]

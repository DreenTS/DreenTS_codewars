"""
LINK: https://www.codewars.com/kata/52b7ed099cdc285c300001cd/

Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all
the interval lengths. Overlapping intervals should only be counted once.

Intervals
Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always
be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

Overlapping Intervals
List containing overlapping intervals:

[
   [1,4],
   [7, 10],
   [3, 5]
]
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5],
which has a length of 4.

Examples:
sumIntervals( [
   [1,2],
   [6, 10],
   [11, 15]
] ) => 9

sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] ) => 7

sumIntervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ) => 19

sumIntervals( [
   [0, 20],
   [-100000000, 10],
   [30, 40]
] ) => 100000030
Tests with large intervals
Your algorithm should be able to handle large intervals. All tested intervals are subsets
of the range [-1000000000, 1000000000].
"""

from copy import deepcopy


def sum_of_intervals(intervals):
    arr = deepcopy(intervals)
    arr.sort()
    sum = 0
    temp = arr[0]
    for inter in arr[1:]:
        if inter[1] >= temp[1] > inter[0] or temp[1] >= inter[1] > temp[0]:
            arr.pop(arr.index(temp))
            maxim = max(temp[1], inter[1])
            arr[arr.index(inter)] = (temp[0], maxim)
            temp = (temp[0], maxim)
        else:
            temp = inter
    for inter in arr:
        sum += inter[1] - inter[0]
    return sum


if __name__ == '__main__':
    intervals = [
        [1, 2],
        [6, 10],
        [11, 15]
    ]
    assert sum_of_intervals(intervals=intervals) == 9

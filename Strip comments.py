"""
LINK = https://www.codewars.com/kata/51c8e37cee245da6b40000bd/

Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

    apples, pears # and bananas
    grapes
    bananas !apples

The output expected would be:

    apples, pears
    grapes
    bananas

The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""


def strip_comments(strng, markers):
    res = ""
    for s in strng.split('\n'):
        for marker in markers:
            if marker in s:
                s = s[:s.find(marker)].rstrip()
        res += s + '\n'
    return res[:-1]


if __name__ == '__main__':
    assert strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']) \
           == 'apples, pears\ngrapes\nbananas'
    assert strip_comments('a #b\nc\nd $e f g', ['#', '$']) == 'a\nc\nd'
    assert strip_comments(' a #b\nc\nd $e f g', ['#', '$']) == ' a\nc\nd'

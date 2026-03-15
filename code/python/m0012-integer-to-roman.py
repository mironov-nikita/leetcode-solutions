# Name: Integer to Roman
# Topics: Hash Table, Math, String
# Difficulty: Medium
# Time Complexity: O(1)
# Space Complexity: O(1)
# Link: https://leetcode.com/problems/integer-to-roman/

class Solution(object):
    def intToRoman(self, num):
        result = ""
        d = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        for value, roman in d:
            if num == 0:
                break
            temp = num // value
            result += roman*temp
            num -= value*temp
        return result
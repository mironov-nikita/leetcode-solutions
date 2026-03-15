# Name: Two Sum
# Topics: Arrays, Hash Table
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = i
        for i in range(len(nums)):
            y = target - nums[i]
            if y in seen and seen[y] != i:
                return [i, seen[y]]

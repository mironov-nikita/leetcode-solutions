# Name: 3 Sum
# Topics: Arrays, Two Pointers, Sorting
# Difficulty: Medium
# Time Complexity: O(n^2)
# Space Complexity: O(1) (ignoring sorting)
# Link: https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, n-1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if summ == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left, right = left+1, right-1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[left] == nums[right+1]:
                        right -= 1
                elif summ < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
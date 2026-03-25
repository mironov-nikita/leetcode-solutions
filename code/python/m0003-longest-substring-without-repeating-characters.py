# Name: Longest Substring Without Repeating Characters
# Topics: Sliding Window, HashTable, String
# Difficulty: Medium
# Time Complexity: O(n)
# Space Complexity: O(1) (s consists of English letters, digits, symbols and spaces) 
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        max_len = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

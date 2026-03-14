# Name: longest common prefix
# Difficulty: Easy
# Time Complexity: O(n)  n - all symbols
# Space Complexity: O(m) m - the shortest word
# Link: https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ''
        return prefix
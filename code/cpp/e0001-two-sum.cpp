/*
 * Name: Two Sum
 * Topics: Arrays, Hash Table
 * Difficulty: Easy
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * Link: https://leetcode.com/problems/two-sum/
 */

#include <vector>
#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> hashtable;
        size_t n = size(nums);
        for (int i = 0; i < n; i++) {
            int need = target - nums[i];
            if (hashtable.find(need) != hashtable.end()) {
                return {hashtable[need], i};
            } else {
                hashtable[nums[i]] = i;
            }
        }
        return {0, 0};
    }
};

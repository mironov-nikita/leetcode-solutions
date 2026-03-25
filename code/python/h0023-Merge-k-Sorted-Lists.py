# Name: Merge k Sorted Lists
# Topics: Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort
# Difficulty: Hard
# Time Complexity: O(n*log(n))
# Space Complexity: O(n) 
# Link: https://leetcode.com/problems/merge-k-sorted-lists/description/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq 

class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        for idx, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, idx, l))
        dummy = ListNode()
        curr = dummy
        while heap:
            value, i, l = heapq.heappop(heap)
            curr.next = l
            curr = curr.next
            l = l.next
            if l:
                heapq.heappush(heap, (l.val, i, l))
        return dummy.next

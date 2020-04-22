# 1287. Element Appearing More Than 25% In Sorted Array
# Source:
# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

# Submission 1:
from collections import Counter


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        return cnt.most_common(1)[0][0]

# Submission 2:


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        store = dict()
        n = len(arr)

        for item in arr:
            if item not in store:
                store[item] = 1
            else:
                store[item] += 1

        for k, v in store.items():
            if v > (n / 4):
                return k

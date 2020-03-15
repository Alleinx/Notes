## 3. Longest Substring Without Repeating Characters
## Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Result:
#### Runtime: 48 ms, faster than 92.90% of Python3 online submissions.
#### Memory Usage: 13.1 MB, less than 97.96% of Python3 online submissions.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        length = 0
        current_length = 0
        store = dict()
        left = 0
        for right, value in enumerate(s):

            if value in store:
                current_length = right - left
                length = max(current_length, length)
                
                if left < store[value] + 1:
                    left = store[value] + 1
            
            store[value] = right
                
        current_length = len(s)-left

        return max(length, current_length)

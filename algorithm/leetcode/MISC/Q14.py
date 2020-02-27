# Q14. Longest Common Prefix:
# https://leetcode.com/problems/longest-common-prefix/

# Result:
# Runtime: 20 ms, faster than 99.52% of Python3 online submissions.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions.


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest_common = []
        # Store result

        char_list = zip(*strs)  # O(n)

        for item in char_list:
            # format:(char_1,char_2,....,char_n)
            if len(set(item)) == 1:
                # all elements are the same:
                longest_common.append(item[0])
            else:
                break

        return ''.join(longest_common)

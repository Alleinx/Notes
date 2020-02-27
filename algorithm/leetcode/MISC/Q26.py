# Q26
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        store = nums[0]
        # store previous value

        i = 1
        while i < len(nums):
            try:
                if nums[i] == store:
                    nums.pop(i)
                else:
                    store = nums[i]
                    i += 1
            except IndexError:
                break

        return len(nums)

    # Or you can:
    # def removeDuplicates(self, nums: list[int]) -> int:
    #     nums[:] = sorted(list(set(nums)))
    #     return len(nums)

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Input:            (121, -121, 10)
# Expected output:  (True, False, False)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        invert = str(x)[::-1]
        return str(x) == invert

# Q67. Add Binary
# Source: https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        base_10 = int(a, base=2) + int(b, base=2)
        return bin(base_10)[2:]

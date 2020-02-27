# Q13. Roman to integer
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        look_up = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        i = 0

        char_list = [char for char in s]

        while i < len(char_list):
            if i + 1 >= len(char_list):
                # Last character, just add up.
                total += look_up[char_list[i]]
                return total
            else:
                if char_list[i] == 'I':
                    if char_list[i+1] == 'V':
                        # IV = 4
                        total += 4
                        i += 2
                    elif char_list[i+1] == 'X':
                        # IX = 9
                        total += 9
                        i += 2
                    else:
                        total += look_up[char_list[i]]
                        i += 1
                elif char_list[i] == 'X':
                    if char_list[i+1] == 'L':
                        # XL = 40
                        total += 40
                        i += 2
                    elif char_list[i+1] == 'C':
                        # XC = 90
                        total += 90
                        i += 2
                    else:
                        total += look_up[char_list[i]]
                        i += 1
                elif char_list[i] == 'C':
                    if char_list[i+1] == 'D':
                        # CD = 400
                        total += 400
                        i += 2
                    elif char_list[i+1] == 'M':
                        # CM = 900
                        total += 900
                        i += 2
                    else:
                        total += look_up[char_list[i]]
                        i += 1
                else:
                    total += look_up[char_list[i]]
                    i += 1

        return total

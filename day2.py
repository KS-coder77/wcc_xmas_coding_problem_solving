# Problem 13. Roman to Integer:
# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

# Initialize the result integer
        total = 0
        prev_value = 0

    # Iterate through each character in the Roman numeral
    # string from right to left
        for char in reversed(s):
            value = d[char]

            # If the current value is less than the previous value, subtract it
            if value < prev_value:
                total -= value
            else:
                # Otherwise, add it
                total += value

# Update the previous value for the next iteration
            prev_value = value

        return total

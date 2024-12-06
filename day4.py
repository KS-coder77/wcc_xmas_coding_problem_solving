# Problem 20. Valid parentheses:
# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        # define stack to keep track of opening brackets
        stack = []

        # iterate through each character in string
        matching_bracket = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in matching_bracket.values():
                # if the character is an opening bracket,
                # push it onto the stack
                stack.append(char)
            elif char in matching_bracket:
                # if the character is a closing bracket
                if stack and stack[-1] == matching_bracket[char]:
                    # if the top of the stack matches the closing bracket,
                    # pop the stack (i.e. bracket pair closed)
                    stack.pop()
                else:
                    return False
            else:
                # if the character is neither an opening or closing bracket
                return False

        # if the stack is empty at the end, the string is valid
        return len(stack) == 0

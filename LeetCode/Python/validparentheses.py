# LeetCode # 20 Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
# Example 4:

# Input: s = "([)]"
# Output: false
# Example 5:

# Input: s = "{[]}"
# Output: true
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

from collections import deque
class Solution:
    def isValid(self,s: str)->bool:
        stack = deque()
        for char in s:
            if char == '{' or char == '[' or char == '(':
                stack.append(char)
            elif char == '}':
                if stack and stack[-1] == '{' :
                    stack.pop()
                else:
                    return False
            elif char == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        if stack:
            return False

        return True
a = Solution()
print(a.isValid("()"))
print(a.isValid("()[]{}"))
print(a.isValid("(]"))
print(a.isValid("([)]"))
print(a.isValid("{[]}"))
print(a.isValid("{"))


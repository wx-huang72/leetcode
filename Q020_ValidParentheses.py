"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

33ms, Beats 81.85% of users with Python3
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in '({[':
                stack.append(p)
            else:
        #          continue
                if ((not stack) or 
                    (p == ")" and stack[-1] != "(") or
                    (p == "]" and stack[-1] != "[") or
                    (p == "}" and stack[-1] != "{")):
                    return False
                stack.pop()
        return not stack

        

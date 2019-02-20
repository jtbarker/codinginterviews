#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (35.79%)
# Total Accepted:    509.1K
# Total Submissions: 1.4M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#
class Solution:
    def isValid(self, s: 'str') -> 'bool':
        countparens = 0
        countbrackets = 0
        countcurly = 0
        for i in s:
            if i == "(":
                countparens += 1
            elif i == ")":
                countparens -= 1
            if i == '[':
                countbrackets += 1
            elif i == ']':
                countbrackets -= 1
            if i == '{':
                countcurly += 1
            elif i == '}':
                countcurly -= 1
        if countparens == 0 and countbrackets == 0 and countcurly == 0:
            return True
        else:
            return False


        

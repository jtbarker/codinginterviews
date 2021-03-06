#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (58.77%)
# Total Accepted:    179.9K
# Total Submissions: 306K
# Testcase Example:  '1'
#
# Write a program that outputs the string representation of numbers from 1 to
# n.
# 
# But for multiples of three it should output “Fizz” instead of the number and
# for the multiples of five output “Buzz”. For numbers which are multiples of
# both three and five output “FizzBuzz”.
# 
# Example:
# 
# n = 15,
# 
# Return:
# [
# ⁠   "1",
# ⁠   "2",
# ⁠   "Fizz",
# ⁠   "4",
# ⁠   "Buzz",
# ⁠   "Fizz",
# ⁠   "7",
# ⁠   "8",
# ⁠   "Fizz",
# ⁠   "Buzz",
# ⁠   "11",
# ⁠   "Fizz",
# ⁠   "13",
# ⁠   "14",
# ⁠   "FizzBuzz"
# ]
# 
# 
#
class Solution:
    def fizzBuzz(self, n: 'int') -> 'List[str]':
        rslt = []
        if n == 1:
            return ["1"]
        for i in range(1,n+1):
            if i%5 == 0 and i % 3 == 0:
                rslt.append("FizzBuzz")
            elif i%5 == 0:
                rslt.append("Buzz")
            elif i%3 == 0:
                rslt.append("Fizz")
            else:
                rslt.append(str(i))
        return rslt
        

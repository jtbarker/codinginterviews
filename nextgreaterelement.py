class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = {}
        stack = []
        for num in nums:
            while stack and stack[-1]<num:
                res[stack.pop()] = num
            stack.append(num)
        return [res[x] if x in res else -1 for x in findNums]
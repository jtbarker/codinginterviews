class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: 
            return 0
        prev = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            curr = max(prev + nums[i], nums[i])
            prev = curr
            if maxSum < curr: 
                maxSum = curr

        return maxSum
        
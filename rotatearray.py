class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)  # use modulo to get rid of all k's above length of nums
        nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k] # replace values below k and replace values above k, so if k is 5 and len(nums) is 9 then first part is nums[4:] and second part is nums[:4]
            
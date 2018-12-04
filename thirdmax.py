class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        theMax = max(nums) 
        while(len(nums)>0 and count<3):
            maxN = max(nums)
            nums = [e for e in nums if e!=maxN]
            count+=1
            
        if(count==3):
            return maxN
        else: return theMax
                
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        j=0
        n=0
        for i in nums:
            n=n+i
            nums[j]=n
            j+=1
        
        return nums

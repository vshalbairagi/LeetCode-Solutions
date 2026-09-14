class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in nums:
            c=0
            for j in nums:
                if j==i:
                    c+=1
            if c==1:
                return i

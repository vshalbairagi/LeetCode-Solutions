class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        z=len(nums)
        s=set(nums)
        for i in range(1,z+1):
            if i not in s:
                ans.append(i)
        
            
        return ans

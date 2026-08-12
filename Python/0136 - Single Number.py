class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums=nums
        l=[]
        for i in nums:
            if i not in l:
                l.append(i)
            else:
                l.remove(i)
        
        return l[0]
           

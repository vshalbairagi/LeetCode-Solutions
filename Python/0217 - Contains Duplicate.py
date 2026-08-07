class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.nums=nums
        s=set(nums)
        if len(s) == len(nums):
            return False
        else:
            return True

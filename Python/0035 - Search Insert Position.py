class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums=nums
        self.target= target
        for i in range(0,len(nums)):
            if target == nums[i]:
                return i
            else:
                nums.append(target)
                nums.sort()
                return nums.index(target)

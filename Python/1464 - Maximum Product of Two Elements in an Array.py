import numpy as np
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums=nums
        arr=np.array(nums)
        m=arr.max()
        arr = np.delete(arr, arr.argmax())
        n=arr.max()
        m=m-1
        n=n-1
        return m*n

import numpy as np
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.nums1=nums1
        self.nums2=nums2
        for i in nums2:
            nums1.append(i)

        arr=np.array(nums1)
        arr=np.median(arr)
        return arr

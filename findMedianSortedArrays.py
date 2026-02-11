class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num3=[]
        num3 = nums1 + nums2
        num3.sort()
        n= len(num3)
        if n%2==0:
            s=n//2
            x = num3[s-1] + num3[s]
            median = x/2.0
        else:
            s=n//2
            median = num3[s]
        return median


        

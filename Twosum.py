class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp=0
        for i in range(0, len(nums)):
            temp = nums[i]
            for j in range(0, len(nums)):
                if j != i:
                    sum = temp + nums[j]
                    if (sum==target):
                        return [i,j]

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        max_sum=None
        for i in nums:
            if sum+i>i:
                sum+=i
            else:
                sum=i
            if max_sum<sum:
                max_sum=sum
        return max_sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        freq={}
        for i,value in enumerate(nums):
            needed=target-value
            if needed in freq:
                return [freq[needed],i]
            freq[value]=i
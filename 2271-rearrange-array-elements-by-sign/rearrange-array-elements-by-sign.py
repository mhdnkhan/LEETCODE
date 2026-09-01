class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos=0
        neg=1
        result=[0]*len(nums)
        for i in nums:
            if i>0:
                result[pos]=i
                pos+=2
            else:
                result[neg]=i
                neg+=2
        return result
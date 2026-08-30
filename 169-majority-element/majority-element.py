class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        element=None
        for i in nums:
            if count==0:
                element=i
                count+=1
            elif element==i:
                count+=1
            else:
                count-=1
        return element
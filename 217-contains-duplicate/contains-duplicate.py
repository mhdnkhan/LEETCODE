class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        el=set()
        for i in nums:
            if i in el:
                return True
            el.add(i)
        return False
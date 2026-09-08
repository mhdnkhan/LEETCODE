class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sett=set(nums)
        maxx=0
        for i in sett:
            if i-1 not in sett:
                count=1
                while i+1 in sett:
                    i+=1
                    count+=1
                if count>maxx:
                    maxx=count
        return maxx
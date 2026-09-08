class Solution(object):
    def nextPermutation(self, nums):    
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        pivot=None
        greater=None
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                pivot=i
                for j in range(n-1,i,-1):
                    if nums[j]>nums[i]:
                        greater=j
                        break
                break
        if pivot is None:
            left = 0
            right = n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        else:
            nums[pivot], nums[greater] = nums[greater], nums[pivot]
            left = pivot + 1
            right = n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
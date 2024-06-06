class Solution(object):
    def findMiddleIndex(self, nums):

        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - nums[i] - left
            if left == right:
                return i
            left += nums[i]
        return -1

       


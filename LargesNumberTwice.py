class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        larger = max(nums)
        secondLarger = -1
        largerIndex = 0
        
        for i in range(len(nums)):
            if nums[i] == larger:
                largerIndex = i
        
        for i in range(len(nums)):
            if nums[i] != larger and nums[i] > secondLarger:
                secondLarger = nums[i]
                
        if larger >= 2 * secondLarger:
            return largerIndex
            
        return -1
        

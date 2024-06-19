#Binary Search 

35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle

            elif nums[middle] < target:
                left = middle + 1

            else: 
                right = middle - 1

        return left

Time Complexity: O(log n), where n is the number of elements in the input array nums.

*****

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        missing = len(nums)
        print(missing)
        
        for i in range(len(nums)):
            missing += i - nums[i]
        return missing

Time Complexity: O(n), where n is the length of the nums list

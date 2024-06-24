class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numeros = len(nums)
        j = 0
        for i in range( numeros):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
        print(f"despues: {nums}")

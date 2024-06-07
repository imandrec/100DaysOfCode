class Solution(object):
    def isPalindrome(self, x):
        nums = str(x)
        y = nums[::-1]
        if nums == y:
            return True
        else:
            return False       

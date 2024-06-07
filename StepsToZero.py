class Solution(object):
    def numberOfSteps(self, num):
        times = 0
        while num !=0:
            if num % 2 == 0: 
                num = num/2
                times += 1
            elif num % 2 != 0:
                num = num-1
                times += 1
        return times       

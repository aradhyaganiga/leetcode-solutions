class Solution(object):
    def twoSum(self, nums, target):
        dict = {}  
        for i, num in enumerate(nums):
            key = target - num
            if key in dict:
                return [dict[key], i]
            dict[num] = i
        

        
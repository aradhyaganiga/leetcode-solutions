import functools
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums=list(map(str,nums))
        nums.sort(key=functools.cmp_to_key(lambda a,b:-1 if a+b>b+a else 1))

        if nums[0]=="0":
            return "0"
        
        return "".join(nums)
        

        
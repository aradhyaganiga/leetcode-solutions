class Solution(object):
    def searchInsert(self, nums, target):
        idx=0
        i=0
        length=len(nums)
        if target not in nums:
            while i<length:
                if nums[i]<target:
                    i+=1
                    idx=i
                else:
                    break
        else:
            idx=nums.index(target)
        return idx

        
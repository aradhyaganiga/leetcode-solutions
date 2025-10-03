class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum=float('inf')
        n=len(nums)
        for i in range(n-2):
            l,r=i+1,n-1
            while l<r:
                total_sum=nums[i]+nums[l]+nums[r]
                if abs(total_sum-target)<abs(closest_sum-target):
                    closest_sum=total_sum
                if total_sum<target:
                    l+=1
                elif total_sum>target:
                    r-=1
                else:
                    return total_sum
        return closest_sum
                
        
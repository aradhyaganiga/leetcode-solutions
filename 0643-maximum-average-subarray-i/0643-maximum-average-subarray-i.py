class Solution(object):
    def findMaxAverage(self, nums, k):
        current=0
        for i in range(k):
            current=current+nums[i]
        maxx_avg=float(current)/k
        for j in range(1,len(nums)-k+1):
            current=current-nums[j-1]+nums[j+k-1]
            current_avg=float(current)/k
            if maxx_avg<current_avg:
                maxx_avg=current_avg
        return maxx_avg


        
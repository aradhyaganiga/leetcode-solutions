class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # They given that array has only one solution hence if l and r meets then program stops
        # Sorted array- Hence Two pointer approch
        l=0
        r=len(numbers)-1
        while l<r:
            total=numbers[l]+numbers[r]
            if total==target:
                return [l+1,r+1]

            elif total<target:
                l+=1
            elif total>target:
                r-=1
        return 0
            




        
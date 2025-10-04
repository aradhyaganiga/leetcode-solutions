class Solution(object):
    def reverse(self, num):
        """
        :type x: int
        :rtype: int
        """
        if num<0:
            sign=-1
        else:
            sign=1
        num=abs(num)
        rev=0

        while num>0:
            rem=num%10
            rev=rev*10+rem
            num=num//10
        rev=rev*sign

        if rev<-2**31 or rev>2**31-1:
            return 0
        return rev
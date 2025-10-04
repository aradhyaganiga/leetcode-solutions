class Solution(object):
    def isPalindrome(self, num):
        """
        :type x: int
        :rtype: bool
        """
        temp=num
        rev=0
        while num>0:
            rem=num%10
            rev=rev*10+rem
            num=num//10
        if temp==rev:
            return True
        else:
            return False
        
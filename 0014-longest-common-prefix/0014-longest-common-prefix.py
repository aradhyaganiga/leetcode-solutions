class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix=strs[0]
        n=len(strs)
        for i in range(1,n):
            while strs[i].find(prefix)!=0:
                prefix=prefix[:-1]
                if prefix=="":
                    return ""
        return prefix
                 
            

        
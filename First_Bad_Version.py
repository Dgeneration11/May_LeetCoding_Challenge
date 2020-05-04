# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 0
        last = n
        while(first<=last):
            mid = (first + last)//2
            if isBadVersion(mid-1) == False and isBadVersion(mid) == True:
                return mid
            elif isBadVersion(mid) == False:
                first = mid+1
            else:
                last = mid-1
            
        return 0    
        
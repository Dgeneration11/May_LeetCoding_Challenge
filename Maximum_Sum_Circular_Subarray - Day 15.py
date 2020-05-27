class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        flag = True
        for i in A:
            if i>0:
                flag = False
        if flag:
            return max(A) 
        
        def kadane(A):
            sum_so_far = 0
            max_sum = 0

            for i in A:
                sum_so_far += i
                if(sum_so_far<0):
                    sum_so_far = 0

                max_sum = max(sum_so_far,max_sum)
            return max_sum
        
        max_kadane = kadane(A)
        
        n = len(A)
        max_wrap = 0
        
        for i in range(0,n): 
            max_wrap += A[i] 
            A[i] = -A[i] 
    
        max_wrap += kadane(A)

        return max(max_kadane,max_wrap)
        
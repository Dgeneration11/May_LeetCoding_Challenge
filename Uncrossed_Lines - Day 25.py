def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
        A = [-1] + A
        B = [0] + B
        len_A = len(A)
        len_B = len(B)
        table = [[0 for j in range(len_B)] for i in range(len_A)]
        for i in range(1, len_A):
            for j in range(1, len_B):
                if A[i] == B[j]:
                    table[i][j] = table[i-1][j-1]+1
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])
        return table[-1][-1]
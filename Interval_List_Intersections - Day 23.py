def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i,j,output = 0,0,[]
        while(i<len(A) and j<len(B)):
            a0,b0 = A[i][0],B[j][0]
            a1,b1 = A[i][1],B[j][1]           
            int0,int1 = max(a0,b0),min(a1,b1)
            # ouput.append(int0,int1)
            i, j = (i+1, j) if a1<=b1 else (i, j+1)
            if int0<=int1:  output.append([int0,int1])
        return output
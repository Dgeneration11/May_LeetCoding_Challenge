def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N==1:
            return 1
        trustScore = [0 for _ in range(N+1)]
        
        for p1,p2 in trust:
            trustScore[p1] -=1
            trustScore[p2] +=1
            
        for person in range(N+1):
            if trustScore[person] == N-1:
                return person 
        
        return -1
        
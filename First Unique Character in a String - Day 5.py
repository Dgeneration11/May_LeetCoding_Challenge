    def firstUniqChar(self, s: str) -> int:
        pos = -1
        
        for i in s:
            count = s.count(i)
            # print(count)
            if count == 1:
                pos = s.index(i)
                break
        
        return pos
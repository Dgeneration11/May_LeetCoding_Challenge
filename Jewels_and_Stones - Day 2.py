class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for stone in S:
            for jewell in J:
                if jewell == stone:
                    count += 1
        return count  


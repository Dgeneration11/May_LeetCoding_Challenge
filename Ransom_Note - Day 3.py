class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for note in ransomNote:
            if note not in magazine:
                return False
            magazine = magazine.replace(note,'',1)
        return True    
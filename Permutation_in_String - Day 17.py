class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        k = len(s1)
        from collections import Counter
        d1 = Counter(s1)
        
        # initial window
        window = s2[:k]
        print(window)
        d2 = Counter(window)
        
        # check the intial window 
        if d1 == d2:
            return True
  
        for i in range(len(s2)-k):
        
            # SLIDE THE WINDOW
            # 1 - remove s2[i]
            if d2[s2[i]] == 1:
                del d2[s2[i]]
            elif d2[s2[i]] > 1:
                d2[s2[i]] -= 1
            
            # 2- add s2[i+k]
            if s2[i+k] in d2:
                d2[s2[i+k]] += 1
            else:
                d2[s2[i+k]] = 1
                
            # check after sliding
            if d1 == d2:
                return True
        return False
        
#         s1 = "".join(sorted(list(s1)))
#         k = len(s1)
        
#          # sort the substrings of s2 that are of the same size
#         for i in range(len(s2)): # -- O(n)
#             sub = s2[i:i+k] # -- O(k)
#             sub_str = "".join(sorted(list(sub)))  # ---- [1] 
#             if s1 == sub_str:
#                  return True
#         return False
    
#         s1_counter = Counter(s1)
#         # s2_counter = Counter(s2)
#         length = len(s1)
        
#         for i in range(len(s2)):
#             sub = s[i:i+length]
#             sub_counter = Counter(sub)
            
#             if s1_counter==sub_counter:
#                 return True

#         return False
          
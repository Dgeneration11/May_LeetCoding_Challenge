
def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = 0
        seen = {0:-1}
        
        for i in range(len(nums)):
            current = nums[i]
            if current==0:
                count-=1
            if current==1:
                count+=1
                
            if count in seen:                       # You have been here before
                 result = max(result, i-seen[count]) # Get the furthest distance
            else:                     # You haven't been here before
                     seen[count] = i  # Mark it
                 
        return result
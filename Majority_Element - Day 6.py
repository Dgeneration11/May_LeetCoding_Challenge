class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        # print(counter)
        for i in set(nums):
            if counter.get(i)>len(nums)//2:
                return i
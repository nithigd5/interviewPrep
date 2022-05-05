from typing import List
from collections import defaultdict

class Solution():
    def fourSum(self,nums: List[int], target : int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)
    
    def kSum(self, nums: List[int], target : int, k : int) -> List[List[int]]:
        res = []
        
        if not nums:
            return res

        averageValue = target//k
        
        if nums[0] > averageValue or nums[-1] < averageValue:
            return res

        if k==2:
            return self.twoSum(nums, target)
        
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for subset in self.kSum(nums[i+1:], target - nums[i], k-1):
                    res.append(subset + [nums[i]])
        return res
                   
    def twoSum(self, nums: List[int], target: int)->List[List[int]]:
        res = []
        lo, hi = 0, len(nums)-1
        while(lo<hi):
            sum = nums[lo] + nums[hi]
            if sum < target or (lo > 0 and nums[lo] == nums[hi]):
                lo = lo + 1
            if sum> target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi = hi-1
            else:
                res.append([nums[lo], nums[hi]])
                lo +=1
                hi -=1
        return res
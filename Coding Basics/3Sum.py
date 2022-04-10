from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        
        for n1 in range(n-2):
            if(n1 > 0 and nums[n1] == nums[n1-1]):
                continue
            (n2, n3) = (n1+1, n-1)
            while(n2<n3):
                sum = nums[n1] + nums[n2] + nums[n3]
                if(sum == 0):
                  result.append((nums[n1],nums[n2],nums[n3]))
                  n3-=1
                  while(n2<n3 and nums[n3]==nums[n3+1]):
                      n3 -=1
                elif sum>0:
                    n3 -= 1
                else:
                    n2+=1
        return result
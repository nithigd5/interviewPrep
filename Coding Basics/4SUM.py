from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
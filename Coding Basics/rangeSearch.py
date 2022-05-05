from typing import List


def LowerBound(nums: List[int], target: int, l, r)->int:
    lowerBound = -1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            lowerBound = m
            r = m - 1
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return lowerBound 
    
def HigherBound(nums: List[int], target: int, l, r)->int:

    higherBound = -1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            higherBound = m
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return higherBound 
    

def search(nums: List[int], target: int)->list[int]:
    start = LowerBound(nums, target, 0, len(nums)-1)
    if start ==  -1:
        return [-1, -1]
    range = [start, start]
    end = HigherBound(nums, target, start, len(nums)-1)
    range[1] = end
    return range
    
    
l = [5,7,7,7,7,8,8,8,9,9,9,9,10,10,10]
t = 10
print(search(l, t))
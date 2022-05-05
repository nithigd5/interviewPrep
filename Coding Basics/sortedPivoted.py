from typing import List


def findPivot(nums: List[int]):
    left = 0
    right = len(nums) - 1
    while left<right:
        m = left + (right - left)//2
        if m > left and nums[m] < nums[m-1]:
            return m
        if right > m and nums[m] > nums[m+1]:
            return m+1
        if nums[right] >= nums[m]:
            right = m - 1
        else:
            left = m + 1
    return -1

def search(nums: List[int], target: int):
    p = findPivot(nums)
    l = 0
    r = len(nums) - 1
    if p != -1 and target >= nums[0:p][0]:
        r = p-1
    elif p != -1 :
        l = p
    while l <= r:
        m = (l + r) //2
        if target == nums[m]:
            return m
        elif target > nums[m]:
            l = m + 1
        else:
            r = m - 1
    return -1

def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if left != len(nums) and nums[left] == target:
        return left
    return -1
l = [i for i in range(0, 6)]
# l = l[5:] + l[0:5]
# l = [4,5,6,7,0,1,2]
# l = [1, 3]
# target = 0
# print(search(l, target))
print(binarySearch(l,5))

from typing import List
import runTime

def merge(arr : List, low: int, mid: int, high: int):
    N = high - low + 1
    res = [0 for _ in range(N)]
    l = low
    r = mid + 1
    b = 0
    while l <= mid and r <= high:
        if arr[l] < arr[r]:
            res[b] = arr[l]
            l += 1
        else:
            res[b] = arr[r]
            r += 1
        b += 1
    while l <= mid: 
        res[b] = arr[l] 
        l += 1
        b += 1 
    while r <= high: 
        res[b] = arr[r] 
        r+=1
        b+=1
    # for i in range(N):
    #     arr[low+i] = res[i]
    arr[low:high+1] = res

def mergeSort(arr: List, low: int, high: int):
    if low >= high:
        return
    mid = (high + low) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)

@runTime.dispRunTime
def msort(arr: List):
    high = len(arr) - 1 
    mergeSort(arr, 0, high)

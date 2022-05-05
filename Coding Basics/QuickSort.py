from typing import List
import runTime

def partition(a: List, start: int, end: int) -> int:
    pivot = a[end]
    pIndex = start
    for i in range(start, end):
        if a[i] <= pivot:
            a[i], a[pIndex] = a[pIndex], a[i]
            pIndex += 1
    a[pIndex], a[end] = a[end], a[pIndex]
    return pIndex

def quickSort(a: List, start: int, end: int):
    if start < end:
        pIndex = partition(a, start, end)
        quickSort(a, start, pIndex-1)
        quickSort(a, pIndex+1, end)

@runTime.dispRunTime
def qSort(a):
    quickSort(a, 0, len(a)-1)
    

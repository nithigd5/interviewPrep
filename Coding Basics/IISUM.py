from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n1 = 0
        n2 = len(numbers) - 1
        numbers.sort()
        res = ()
        while(n1<n2):
            t = numbers[n1] + numbers[n2]
            if t==target:
              res = (numbers[n1],numbers[n2])
              n2 -=1
              break
            elif t>target:
                n2-=1
            else:
                n1 +=1
        return res
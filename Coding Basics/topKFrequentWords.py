from heapq import nlargest
from queue import PriorityQueue
from typing import Counter, List

from numpy import integer

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
      pq = PriorityQueue()
      countMap = Counter(words)
      # countMap = dict()
      # for i in words:
      #    if countMap.get(i, False):
      #       countMap[i] += 1
      #    else:
      #       countMap[i] = 1
      for item,count in countMap.items():
         pq.put((-count, item))
      
      res = []
      while k>0:
         res.append(pq.get()[1])
         k -= 1
      return res

words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
words = ["i","love","leetcode","i","love","coding"]
k = 4
words = ['z', 'z', 'x', 'x','a','c','c']
print(Solution().topKFrequent(words, k))
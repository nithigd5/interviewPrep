from collections import deque
from re import L
from typing import List

from Graph import AdjacencyGraph

class Solution:
    def BFS(self, graph, s, i):
        q = deque()
        if i in s:
            return False
        q.append(i)
        res = 0
        while q:
            c = q.popleft()
            if c not in s:
                s.add(c)
                res += 1
            for adj in graph.adjList[c]:
                if adj not in s:
                    q.append(adj)
        return res
    def numIslands(self, grid : List[List[str]]) -> int:
        graph = AdjacencyGraph(grid)
        count  = 0
        s = set()
        for i in graph.nodes:
            if i not in s:
                if(self.BFS(graph, s, i)> 0 ):
                    count += 1
        return count
    
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
grid = [["0"]]
grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]

grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
grid = [["1","0","1","1","0","1","1"]]
print(Solution().numIslands(grid))
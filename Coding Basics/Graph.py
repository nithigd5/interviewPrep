from typing import List

class Graph:
	def __init__(self, edges, n, directed = False):
		self.adjList = [[] for _ in range(n)]
		for (src, dest) in edges:
			self.adjList[src].append(dest)
			if not directed:
				self.adjList[dest].append(src)


class AdjacencyGraph:
	def __init__(self, grid: List[List[str]]):
		n = len(grid)
		m = len(grid[0])
		self.adjList = [[] for i in range(max(n, m))]
		self.nodes = set()
		for i in range(n):
			for j in range(m):
				if grid[i][j] == '1' and j not in self.adjList[i]:
					self.adjList[i].append(j)
					self.nodes.add(j)
	def getGraphData(self):
		for i in self.nodes:
			for j in self.adjList[i]:
				if i != j:
					print("{0} {1}".format(i,j))
				else:
					print(j)

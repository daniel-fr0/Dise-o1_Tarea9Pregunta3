# Programa basado en la solucion de GeeksforGeeks
# https://www.geeksforgeeks.org/introduction-and-approximate-solution-for-vertex-cover-problem/
from collections import defaultdict

class Graph:
	def __init__(self):
		self.V = set()
		self.graph = defaultdict(list)

	def add(self, u, v):
		self.V.update({u, v})
		self.graph[u].append(v)

	def edges(self):
		for u in self.graph:
			for v in self.graph[u]:
				yield u, v

	# Funcion de minCover, toma O(V + E) tiempo
	def minCover(self):
		# Conjunto resultado
		result = set()

		# Vertices visitados
		visited = {v: False for v in self.V}		# O(V)
		
		# Se consideran todas las aristas una por una
		# Se agregan los vertices no visitados al conjunto de vertices cubiertos
		for (u, v) in self.edges():					# O(E)
			if not visited[u] and not visited[v]:
				result.update({u, v})
				visited[u] = visited[v] = True

		return result

if __name__ == "__main__":
	g = Graph()
	g.add(0, 1)
	g.add(0, 2) 
	g.add(1, 3) 
	g.add(3, 4) 
	g.add(4, 5) 
	g.add(5, 6) 

	print(g.minCover())

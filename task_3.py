import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(self.V)}

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight)) 

    def dijkstra(self, src):
        heap = []
        distances = {i: float('inf') for i in range(self.V)}
        distances[src] = 0
        heapq.heappush(heap, (0, src))

        while heap:
            current_distance, u = heapq.heappop(heap)

            if current_distance > distances[u]:
                continue

            for neighbor, weight in self.graph[u]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances

g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

source = 0
distances = g.dijkstra(source)
print(f"Найкоротші відстані від вершини {source}:")
for vertex, distance in distances.items():
    print(f"Вершина {vertex} : Відстань {distance}")

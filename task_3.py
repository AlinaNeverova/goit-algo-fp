import networkx as nx
import heapq

# Створення орієнтованого зваженого графа
DG = nx.DiGraph()
# Додаємо вершини та ребра з вагами
DG.add_edge('A', 'B', weight=2)
DG.add_edge('A', 'C', weight=3)
DG.add_edge('B', 'C', weight=1)
DG.add_edge('B', 'D', weight=4)
DG.add_edge('C', 'D', weight=2) 

# Створення алгоритму Дейкстри із використанням купи
def dijkstra_heap(DG, start):
    distances = {node: float('inf') for node in DG.nodes}
    distances[start] = 0

    queue = [(0, start)]
    visited = set()

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor in DG.neighbors(current_node):
            weight = DG[current_node][neighbor].get('weight', 1)
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    return distances

# Використання алгоритму Дейкстри
result = dijkstra_heap(DG, 'A')
print(result) # Результат {'A': 0, 'B': 2, 'C': 3, 'D': 5}
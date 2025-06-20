import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import deque

# Побудова бінарного дерева за кодом з умови
class Node:
	def __init__(self, key, color="#1296F0"):
		self.left = None
		self.right = None
		self.val = key
		self.color = color
		self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
	if node is not None:
		graph.add_node(node.id, color=node.color, label=node.val)
		if node.left:
			graph.add_edge(node.id, node.left.id)
			l = x - 1 / 2 ** layer
			pos[node.left.id] = (l, y - 1)
			add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
		if node.right:
			graph.add_edge(node.id, node.right.id)
			r = x + 1 / 2 ** layer
			pos[node.right.id] = (r, y - 1)
			add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
	return graph

def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(9, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_size=10)
    plt.show()

# Зв'язуємо id вузлів з об'єктами Node для подальшої зміни кольору
def get_node_map(root):
    node_map = {}
    queue = deque([root])
    while queue:
        current = queue.popleft()
        node_map[current.id] = current
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return node_map

# Побудова словника суміжності для обходу
def build_graph_dict(node):
    graph = {}
    queue = deque([node])
    while queue:
        current = queue.popleft()
        graph[current.id] = []
        if current.left:
            graph[current.id].append(current.left.id)
            queue.append(current.left)
        if current.right:
            graph[current.id].append(current.right.id)
            queue.append(current.right)
    return graph

# Градієнт кольорів для візуалізації
def generate_color_gradient(n, base_color="#1296F0"):
    base = mcolors.to_rgb(base_color)
    gradient = []
    for i in range(n):
        factor = i / max(n - 1, 1)
        new_color = tuple(base[j] + (1.0 - base[j]) * factor for j in range(3))
        gradient.append(mcolors.to_hex(new_color))
    return gradient

# Функції обходу дерева DFS, BFS
def dfs(node, node_map):
    graph = build_graph_dict(node)
    stack = [node.id]
    visited = []
    seen = set()
    while stack:
        current = stack.pop()
        if current not in seen:
            visited.append(current)
            seen.add(current)
            for neighbor in reversed(graph.get(current, [])):
                stack.append(neighbor)
    gradient = generate_color_gradient(len(visited), base_color="#1296F0")
    for idx, node_id in enumerate(visited):
        node_map[node_id].color = gradient[idx]
			
def bfs(node, node_map):
    graph = build_graph_dict(node)
    queue = deque([node.id])
    visited = []
    seen = set()
    while queue:
        current = queue.popleft()
        if current not in seen:
            visited.append(current)
            seen.add(current)
            for neighbor in graph.get(current, []):
                queue.append(neighbor)
    gradient = generate_color_gradient(len(visited), base_color="#F07F13")
    for idx, node_id in enumerate(visited):
        node_map[node_id].color = gradient[idx]

# Побудова дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# DFS
node_map_dfs = get_node_map(root)
dfs(root, node_map_dfs)
draw_tree(root, title="DFS")

# BFS (додаткове дерево, щоб не перекривати кольори DFS)
root_bfs = Node(0)
root_bfs.left = Node(4)
root_bfs.left.left = Node(5)
root_bfs.left.right = Node(10)
root_bfs.right = Node(1)
root_bfs.right.left = Node(3)

node_map_bfs = get_node_map(root_bfs)
bfs(root_bfs, node_map_bfs)
draw_tree(root_bfs, title="BFS")
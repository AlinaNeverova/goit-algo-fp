import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Беремо за основу код із завдання
class Node:
	def __init__(self, key, color="skyblue"):
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
			l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
		if node.right:
			graph.add_edge(node.id, node.right.id)
			r = x + 1 / 2 ** layer
			pos[node.right.id] = (r, y - 1)
			r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
	return graph

def draw_tree(tree_root):
	tree = nx.DiGraph()
	pos = {tree_root.id: (0, 0)}
	tree = add_edges(tree, tree_root, pos)

	colors = [node[1]['color'] for node in tree.nodes(data=True)]
	labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

	plt.figure(figsize=(8, 5))
	nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
	plt.show()

# Додаємо функцію для побудови дерева з купи
def build_heap_tree(heap, index=0):
    if index >= len(heap):
        return None
    node = Node(heap[index])
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    node.left = build_heap_tree(heap, left_index)
    node.right = build_heap_tree(heap, right_index)
    return node

# Візуалізуємо дерево з купи
heap = [7, 3, 8, 1, 2, 6]
heapq.heapify(heap)
heap_root = build_heap_tree(heap)
draw_tree(heap_root)
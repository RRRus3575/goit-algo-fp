import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
import heapq

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

def draw_tree(tree_root, pos, ax, title):
    tree = nx.DiGraph()
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    ax.clear()
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    ax.set_title(title)
    return tree

def build_heap_tree(heap):
    if not heap:
        return None

    nodes = [Node(val) for val in heap]
    for i in range(len(nodes)):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

def get_color_gradient(n):
    colors = []
    for i in range(n):
        shade = int(255 * i / (n - 1))
        colors.append('#{:02X}{:02X}FF'.format(shade, 255 - shade))
    return colors

def bfs(root):
    if root is None:
        return []

    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        visited.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited

def dfs(root):
    if root is None:
        return []

    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited

def animate_traversal(traversal, pos, title):
    colors = get_color_gradient(len(traversal))

    fig, ax = plt.subplots(figsize=(8, 5))

    def update(num):
        if num > 0:
            prev_node = traversal[num - 1]
            prev_node.color = colors[num - 1]

        current_node = traversal[num]
        current_node.color = 'red'  # Колір для поточного відвідуваного вузла

        draw_tree(traversal[0], pos, ax, f"{title}: Step {num + 1}")

    ani = FuncAnimation(fig, update, frames=len(traversal), repeat=False)
    plt.show()

heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heapq.heapify(heap)

root = build_heap_tree(heap)

pos = {root.id: (0, 0)}
add_edges(nx.DiGraph(), root, pos)

bfs_traversal = bfs(root)
animate_traversal(bfs_traversal, pos, "BFS Traversal")

dfs_traversal = dfs(root)
animate_traversal(dfs_traversal, pos, "DFS Traversal")

# Prin algorith allows us to start from a node we choose
# kuskow - need to build a tree from every node and join them afterwards

from queue import PriorityQueue

class Edge():
    def __init__(self, first, second, distance):
        self.first = first
        self.second = second
        self.distance = distance

    def __gt__(self, other):
        return self.distance > other.distance


def calc_damage(jumps, damage):
    for _ in range(jumps):
        damage = damage // 2

    return damage


def prim(node, damage, damage_by_node, graph):
    damage_by_node[node] += damage

    tree = {node}
    jumps = [0] * len(graph)

    pq = PriorityQueue()
    # put all children to the node we start from (hot by lightning)
    for edge in graph[node]:
        pq.put(edge)

    while not pq.empty():
        min_edge = pq.get()

        tree_node, non_tree_node = -1, -1

        # check if node is in the tree, if not connect it
        if min_edge.first in tree and min_edge.second not in tree:
            tree_node = min_edge.first
            non_tree_node = min_edge.second
        
        elif min_edge.second in tree and min_edge.first not in tree:
            tree_node = min_edge.second
            non_tree_node = min_edge.first
        
        if non_tree_node == -1:
            continue # we dont use this node


        
        #if the node is not in the tree set, we add it
        tree.add(non_tree_node)
        # and add to the Priority Queue all this nodes children
        [pq.put(edge) for edge in graph[non_tree_node]]


        jumps[non_tree_node] = jumps[tree_node] + 1
        damage_by_node[non_tree_node] += calc_damage(jumps[non_tree_node], damage)




nodes = int(input())
edges = int(input())
lightnings = int(input())

graph = {node: [] for node in range(nodes)}

for _ in range(edges):
    first, second, distance = [int(x) for x in input().split()]
    edge = Edge(first, second, distance)

    graph[first].append(edge)
    graph[second].append(edge)


damage_by_node = [0] * nodes
for _ in range(lightnings):
    node, damage = [int(x) for x in input().split()]

    prim(node, damage, damage_by_node, graph)

print(max(damage_by_node))
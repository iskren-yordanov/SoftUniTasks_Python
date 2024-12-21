from collections import deque
from queue import PriorityQueue

class Edge():
    def __init__(self, first, second, weight, is_open):
        self.first = first
        self.second = second
        self.weight = weight
        self.is_open = is_open

roads_n = int(input())
graph = {}

for _ in range(roads_n):
    first, second, weight_s = input().split(' - ')
    weight = int(weight_s)

    if first not in graph:
        graph[first] = []

    if second not in graph:
        graph[second] = []

    graph[first].append(Edge(first, second, weight, 1))
    graph[second].append(Edge(second, first, weight, 1))

closed_road = input()

starting_city = input()
target_city = input()

#print(closed_road)

list_closed = closed_road.split(',')

# we remove the path - or update it to a tooo big number so its not used
for el in list_closed:
    first, second = el.split('-')
    #print(first, second)

    for chld in graph[first]:
        if chld.first == first and chld.second == second:
            #chld.weight = 100000
            chld.is_open = 0

    for chld in graph[second]:
        if chld.first == second and chld.second == first:
            #chld.weight = 100000
            chld.is_open = 0


# we can use Djinkstra since they are positive numbers (distance)
distance = {} 
parent = {}

cnt_nodes = len(graph.keys())
for i in graph.keys():
    distance[i] = float('inf')
    parent[i] = i

distance[starting_city] = 0

pq = PriorityQueue()
pq.put((0, starting_city))

while not pq.empty():
    min_distance, node = pq.get()

    # reached the end
    if node == target_city:
        break

    for edge in graph[node]:
        # if load is not open, then move one and not use it
        if edge.is_open != 1:
            continue
        
        new_distance = min_distance + edge.weight
        if new_distance < distance[edge.second]:
            distance[edge.second] = new_distance
            parent[edge.second] = node

            pq.put((new_distance, edge.second))

#print(distance[target_city])

if distance[target_city] == float('inf'):
    print('Cities are not connected.')
else:
    
    path = deque()
    node = target_city

    while node is not None and node != starting_city:
        path.appendleft(node)
        node = parent[node]

    # add final city (the starting_citying one)
    path.appendleft(starting_city)

    # print result
    print(*path, sep =' - ')
    print(distance[target_city])
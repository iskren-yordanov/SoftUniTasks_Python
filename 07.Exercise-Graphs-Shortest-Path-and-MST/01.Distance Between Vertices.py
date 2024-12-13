from collections import deque

def find_shortest_path(graph, source, destination):
    
    queue = deque([source])
    visited = {source}

    parrent = {source: None}

    while queue:
        node = queue.popleft()

        if node == destination:
            break

        for child in graph[node]:
            if child in visited:
                continue

            queue.append(child)
            visited.add(child)

            parrent[child] = node
    
    return parrent

def find_path_size(parrent, destination):
    
    size = 0
    node = destination

    while node is not None:
        node = parrent[node]
        size += 1

    return size -1



nodes = int(input())
pairs = int(input())

graph = {}


for _ in range(nodes):
    node_str, children_str = input().split(':')

    node = int(node_str)
    children = [int(x) for x in children_str.split()] if children_str else []

    graph[node] = children



for _ in range(pairs):
    source, destination = [int(x) for x in input().split('-')]

    parrent = find_shortest_path(graph, source, destination)
    # this is a dict, that has the node and its parrent, so we trace from end till we reach the start to get the path
    #print(parrent)

    if destination not in parrent:
        print(f'{{{source}, {destination}}} -> -1')
        continue

    size = find_path_size(parrent, destination)
    
    print(f'{{{source}, {destination}}} -> {size}')


# Sample input
# 8
# 4
# 1:4
# 2:4
# 3:4 5
# 4:6
# 5:3 7 8
# 6:
# 7:8
# 8:
# 1-6
# 1-5
# 5-6
# 5-8

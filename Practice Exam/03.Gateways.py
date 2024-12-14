from collections import deque

def dfs(node, end, graph, visited, ):
    if node in visited:
        return
    
    visited.append(node)
    if node == end:
        return

    for child in graph[node]:
        dfs(child, end, graph, visited)

def bfs(node, end, graph, visited, lenf):
    if node in visited:
        return

    if node == end:
        return

    queue = deque([node])
    
    if lenf < len(visited):
        return

    visited.add(node)
    
    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')
        
        for child in graph[current_node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)



def find_parent_by_node(graph, start_node, destination_node):
    visited = [False] * len(graph)
    parent = [None] * len(graph)

    visited[start_node] = True
    queue = deque([start_node])

    while queue:
        node = queue.popleft()

        if node == destination_node:
            break

        for child in graph[node]:
            if visited[child]:
                continue

            visited[child] = True
            queue.append(child)

            parent[child] = node

    return parent

def reconstruct_path(parent, destination_node):
    path = deque()

    node = destination_node
    while node is not None:
        path.appendleft(node)
        node = parent[node]

    return path





nodes = int(input())
edges = int(input())

graph = [[] for _ in range(nodes + 1)]

for _ in range(edges):
    start_str, end_str = input().split()
    start = int(start_str)
    end = int(end_str)

    
    graph[start].append(end)
    

#print(graph)

begin = int(input())
ending = int(input())

# mark all visited
parent = find_parent_by_node(graph, begin, ending)

#print(len(queue))
path = reconstruct_path(parent, ending)

#print(f'Shortest path length is: {len(path) - 1}')
print(*path, sep = ' ')

#print(*visited, sep=' ')


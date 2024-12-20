from collections import deque

def dfs(node, graph, visited, result):
    if node in visited:
        return
    
    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited, result)
    
    result.appendleft(node)

graph = {}

while True:
    line = input()

    if line == 'End':
        break

    node, children_str =  [x.strip() for x in line.split('->')]
    children = children_str.split()

    graph[node] = children

    #for child in children:
    #    graph[child] = []

# we triger a dpf
visited = set()
result = deque()

for node in graph:
    dfs(node, graph, visited, result)

#result = reversed(result)
print(*result, sep =' ')

def dfs(node, graph, visited):
    if node in visited:
        return
    
    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited)

nodes = int(input())
edges = int(input())

# create empty graph
graph = {node: [] for node in range(1, nodes + 1)}

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())

# mark all visited
visited = set()
dfs(start_node, graph, visited)

# find not visited:
unreachable_node = []

for node in graph.keys():
    if node not in visited:
        unreachable_node.append(node)

print(*sorted(unreachable_node), sep=' ')





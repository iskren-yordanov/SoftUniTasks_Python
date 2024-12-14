#Task 1

def dfs(node, graph, visited):
    if visited[node]:
        return
    
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)
        
    print(node, end=' ')
    
el = int(input())
graph = []

for _ in range(el):
    line = input()
    children = [] if line == '' else [int(x) for x in line.split()] 
    graph.append(children)
    
#print(graph)

#graph = [
#    [3, 6],
#    [3, 4, 5, 6],
#    [8],
#    [0, 1, 5],
#    [1, 6],
#    [1, 3],
#    [0, 1, 4],
#    [],
#    [2]
#]



visited = [None] * len(graph)

for node in range(len(graph)):
    if visited[node] is None:
        print(f'Connected component: ', end = '')
        dfs(node, graph, visited)
        print()
    else:
        continue
#Task 1 # other appproach with a component to keep track of the list of nodes per graph

def dfs(node, graph, visited, component):
    if visited[node]:
        return
    
    visited[node] = True
    
    for child in graph[node]:
        dfs(child, graph, visited, component)
        
    #print(node, end=' ')
    component.append(node)
    
el = int(input())
graph = []

for _ in range(el):
    line = input()
    children = [] if line == '' else [int(x) for x in line.split()] 
    graph.append(children)
    
#print(graph)

graph = [
    [3, 6],
    [3, 4, 5, 6],
    [8],
    [0, 1, 5],
    [1, 6],
    [1, 3],
    [0, 1, 4],
    [],
    [2]
]

visited = [False] * len(graph)

for node in range(len(graph)):
    if visited[node] == False:
        component = []
        dfs(node, graph, visited, component)
        
        print(f"Connected component: {' '.join([str(x) for x in component])}", end = '')
        print()
    else:
        continue
def search_for_the_path(row, col, lab, depth, final_path):
    # check maze constarints
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return
    
    # if we have a wall or its already used we cant use it
    if (lab[row][col] == '#') or (lab[row][col] == 'V'):
        return
    
    # if we reached the end finalize the search
    if (lab[row][col] == 'E'):
        final_path.append(depth)
            
    else:
        # mark as visited (V)
        lab[row][col] = 'V'
        search_for_the_path(row, col + 1, lab, depth+1, final_path) # Right
        search_for_the_path(row, col - 1, lab, depth+1, final_path) # Left
        search_for_the_path(row + 1, col, lab, depth+1, final_path) # Down
        search_for_the_path(row - 1, col, lab, depth+1, final_path) # Up
        lab[row][col] = '.'
    
rows = int(input())

# read the matrix
matrix = []
for _ in range(rows):
    matrix.append(list(input()))

# if we get multiple solutions, we will save them in a list, and then find the best one.
# The task does not want the path, so we are not required to save it, just count  
path = []
search_for_the_path(0, 0, matrix, 0, path)

if len(path) == 0:
    print('No path found')
else:
    min_path = path[0]
    for el in range(1, len(path)):
        if min_path> path[el]:
            min_path = path[el]

print(min_path)
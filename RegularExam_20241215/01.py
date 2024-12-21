def search_for_the_path(row, col, lab, direction, path, final_path):
    # check maze constarints
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return
    
    # if we have a wall or its already used we cant use it
    if (lab[row][col] == '#') or (lab[row][col] == 'V'):
        return
    
    path.append(direction)
    
    # if we reached the end finalize the search
    if (lab[row][col] == 'E'):
        final_path.append(list(path))
        #print(''.join(path))
        
    else:
        lab[row][col] = 'V'
        search_for_the_path(row, col + 1, lab, 'R', path, final_path)
        search_for_the_path(row, col - 1, lab, 'L', path, final_path)
        search_for_the_path(row + 1, col, lab, 'D', path, final_path)
        search_for_the_path(row - 1, col, lab, 'U', path, final_path)
        lab[row][col] = '.'
    
    path.pop()
    
rows = int(input())

# read the matrix
matrix = []
for _ in range(rows):
    matrix.append(list(input()))


#print(matrix)    
path = []
search_for_the_path(0, 0, matrix, '', [], path)

min_path = +1000
for el in path:
    if min_path > (len(el) - 1): # len - 1 since the initial starting of the search is ''
        min_path = len(el) - 1
print(min_path)
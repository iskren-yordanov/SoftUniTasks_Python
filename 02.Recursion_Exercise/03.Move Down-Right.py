#Recursion Excersize 3
def count_all_paths(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0
    
    if row == rows -1 and col == cols - 1:
        return 1
    
    result = 0
    result += count_all_paths(row, col + 1, rows, cols) # Right
    result += count_all_paths(row + 1, col, rows, cols) # Down
    
    return result

rows = int(input())
cols = int(input())

print(count_all_paths(0, 0, rows, cols))
    
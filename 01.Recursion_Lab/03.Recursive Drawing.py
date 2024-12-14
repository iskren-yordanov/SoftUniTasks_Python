#Recursion Lab task 3
def draw(cnt):
    if (cnt > 0):
        print('*' * (cnt))
        draw(cnt-1)
        print('#' * (cnt))
    
draw(int(input()))
#Recursion Lab task 4
def gen01(idx, vector):
    if idx >= len(vector):
            print(*vector, sep = '')
            return
    
    for number in range(0, 2):
        vector[idx] = number
        gen01(idx + 1, vector)
        

n = int(input())
vector = [0] * n
        
gen01(0, vector)
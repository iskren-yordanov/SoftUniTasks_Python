#Recursion Lab task 2
def calc_fact(numb):
    if numb == 1:
        return 1
    return numb * calc_fact(numb - 1)

n = int(input())
print(calc_fact(n))
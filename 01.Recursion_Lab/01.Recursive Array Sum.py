#Recursion Lab task 1
def calc_sum(numbers, idx):
	if (idx == len(numbers) -1):
		return numbers[idx]
	return numbers[idx] + calc_sum(numbers, idx+1)
        

my_nums = [int(x) for x in input().split()]
print(calc_sum(my_nums,0))
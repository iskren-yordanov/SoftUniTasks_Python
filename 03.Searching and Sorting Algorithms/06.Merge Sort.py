#Searching and Sorting Algorithms task 5 Merge sort

def merge_arrays(left, right):
    result = []
    
    left_idx = 0
    right_idx = 0
    
    while left_idx < len(left) and right_idx < len(right):
        if (left[left_idx] < right[right_idx]):
            result.append(left[left_idx])
            left_idx +=1
        else:
            result.append(right[right_idx])
            right_idx +=1

    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx +=1

    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx +=1

    return result
            
    
def merge_sort(nums):
    if len(nums) == 1:
        return nums
    
    mid_idx = len(nums) // 2
    
    left = nums[:mid_idx]
    right = nums[mid_idx:]
    
    return merge_arrays(merge_sort(left), merge_sort(right))



nums = [int(x) for x in input().split()]
sorted_arr = merge_sort(nums)
print(*sorted_arr, sep=' ')
from collections import deque

nums = [int(x) for x in input().split(', ')]

size = [0] * len(nums)
size[0] = 1

parent = [None] * len(nums)

best_idx = 0
best_choise = 1


for current_position in range (1, len(nums)):
    current_position_number = nums[current_position]
    current_position_best_choise = 1
    current_position_parent = None

    for prev in range(current_position - 1, -1, -1):
        prev_number = nums[prev]
        
        if prev_number > current_position_number:
            continue

        if size[prev] + 1 >= current_position_best_choise:
            current_position_best_choise = size[prev] + 1
            current_position_parent = prev

    size[current_position] = current_position_best_choise
    parent[current_position] = current_position_parent

    if current_position_best_choise > best_choise:
        best_choise = current_position_best_choise
        best_idx = current_position


# use deque to find the path of the common increasing subsequence
SubSeqResult = deque()

while best_idx is not None:
    SubSeqResult.appendleft(nums[best_idx])
    best_idx = parent[best_idx]

# print result
print(*SubSeqResult, sep=' ')


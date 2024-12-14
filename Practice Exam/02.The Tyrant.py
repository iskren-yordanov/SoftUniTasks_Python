from collections import deque

nums = [int(x) for x in input().split()]

lists = [[] for _ in range(len(nums))]
visited = [False for _ in range(len(nums))]
#print(visited)

for idx in range(len(nums)):
    current = nums[idx]
    if visited[idx] == False:
        lists[idx].append(nums[idx])
        visited[idx] = True
    
        for idx2 in range(idx+1, len(nums)):
            if len(lists[idx]) == 4:
                break

            if nums[idx2] > current:
                if visited[idx2] == False:
                    lists[idx].append(nums[idx2])
                    current = nums[idx2]
                    visited[idx2] = True
        

ids_to_top = deque()

for idx in range(len(lists)):
    if len(lists[idx]) < 4:
        ids_to_top.appendleft(idx)
        #del lists[idx]

for idx in ids_to_top:
    del lists[idx]

#print(lists)
sum = 0
for el in lists:
    sum+= min(el)
print(sum)

# 1 2 3 4 5 6 7 8
# Longest increasing subsequence algorithm

from collections import deque

words = input().split()

size = [0] * len(words)
prev = [0] * len(words)

best_size = 0
best_idx = 0

for idx in range(len(words)):
    current_word = words[idx]
    current_size = 1
    parent = None

    for prev_idx in range(idx - 1, -1, -1):
        prev_word = words[prev_idx]

        if len(prev_word) >= len(current_word):
            continue # we cant create a longer sub sequence

        # we are moving TO THE LEFT, so = will move to the most left one
        if size[prev_idx] + 1 >= current_size:
            current_size = size[prev_idx] + 1
            parent = prev_idx
    
    size[idx] = current_size
    prev[idx] = parent

    if current_size > best_size:
        best_size = current_size
        best_idx = idx

result = deque()

idx_vis = best_idx
while idx_vis is not None:
    result.appendleft(words[idx_vis])
    idx_vis = prev[idx_vis]

print(*result)

            
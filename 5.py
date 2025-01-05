from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    # Step 1: Initialize the queue with all rotten oranges and count fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_count += 1

    # Directions for 4-adjacency (up, down, left, right)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    minutes = 0

    # Step 2: Perform BFS
    while queue and fresh_count > 0:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2  # Rot the fresh orange
                    fresh_count -= 1  # Decrease the fresh orange count
                    queue.append((nx, ny))
        minutes += 1

    # Step 3: Check if all fresh oranges are rotted
    return minutes if fresh_count == 0 else -1

grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
print(oranges_rotting(grid))  # Output: 4

#778. Swim in Rising Water
#https://leetcode.com/problems/swim-in-rising-water/


import time
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        n = len(grid)
        p = list(range(n * n))
        hi = [0] * (n * n)
        for i, row in enumerate(grid):
            for j, h in enumerate(row):
                hi[h] = i * n + j
        for t in range(n * n):
            i, j = hi[t] // n, hi[t] % n
            for a, b in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                x, y = i + a, j + b
                if 0 <= x < n and 0 <= y < n and grid[x][y] <= t:
                    p[find(x * n + y)] = find(hi[t])
            if find(0) == find(n * n - 1):
                return t
        return -1


test_cases = [
    # ([[43, 45, 19, 20, 19, 23, 5], [36, 29, 40, 42, 20, 39, 5], [4, 42, 44, 31, 23, 32, 47], [27, 30, 8, 7, 32, 45, 31], [17, 45, 34, 9, 16, 7, 48], [38, 25, 40, 30, 3, 46, 6], [39, 25, 23, 2, 19, 13, 37]], 41),
    ([[33, 37, 32, 31, 38, 3, 12], [38, 17, 8, 44, 5, 7, 16], [33, 44, 4, 33, 28, 41, 17], [42, 14, 46, 37, 12, 14, 8], [12, 28, 16, 41, 17, 28, 7], [1, 40, 21, 7, 35, 16, 21], [46, 27, 36, 16, 5, 14, 40]], 44),
    ([[4, 9, 14, 5], [8, 6, 12, 7], [3, 12, 10, 3], [0, 5, 14, 0]], 12),
    ([[32, 19, 20, 2, 14, 20], [19, 14, 25, 18, 19, 8], [8, 33, 11, 0, 14, 17], [35, 15, 31, 6, 17, 29], [8, 24, 29, 17, 29, 18], [28, 7, 0, 5, 29, 12]], -1),
    ([[9, 18, 19, 76, 32, 16, 29, 68, 12], [55, 28, 25, 20, 22, 46, 54, 9, 25], [55, 21, 68, 20, 38, 67, 49, 70, 10], [27, 37, 40, 33, 65, 64, 60, 1, 57], [75, 30, 32, 1, 34, 80, 67, 34, 26], [61, 39, 35, 33, 79, 20, 9, 44, 76], [73, 33, 11, 58, 67, 47, 38, 12, 13], [66, 25, 54, 60, 21, 22, 79, 46, 47], [19, 21, 25, 75, 80, 78, 17, 56, 61]], 78),
    ([[17, 9, 7, 8, 17], [10, 12, 3, 15, 1], [4, 19, 20, 19, 8], [9, 12, 6, 4, 20], [12, 15, 11, 5, 11]], -1),
    ([[31, 61, 41, 15, 52, 51, 4, 25], [43, 42, 23, 31, 24, 0, 22, 59], [50, 30, 47, 60, 6, 12, 23, 30], [11, 36, 8, 52, 36, 24, 51, 17], [41, 60, 9, 18, 7, 41, 56, 31], [37, 33, 14, 48, 11, 39, 60, 28], [34, 22, 32, 53, 38, 50, 53, 36], [32, 3, 17, 17, 38, 0, 40, 17]], 47),
    ([[51, 42, 55, 46, 8, 45, 21, 42], [53, 5, 21, 37, 43, 63, 35, 11], [18, 11, 10, 42, 7, 17, 2, 42], [26, 40, 62, 12, 46, 1, 40, 12], [33, 57, 39, 10, 1, 38, 34, 12], [13, 29, 24, 27, 26, 51, 14, 9], [35, 56, 4, 5, 34, 29, 39, 22], [45, 60, 60, 10, 36, 15, 13, 48]], 53),
    ([[5, 1, 8], [1, 8, 7], [2, 8, 2]], -1),
    ([[2, 0], [3, 3]], 3)
]


sol = Solution()
total_time = 0.0

for grid, expected in test_cases:
    start_time = time.perf_counter()
    result = sol.swimInWater(grid)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    assert result == expected, f"Test failed for grid({grid}). Expected {expected}, got {result}"
    print(f"Test passed for grid=({grid}). Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")      
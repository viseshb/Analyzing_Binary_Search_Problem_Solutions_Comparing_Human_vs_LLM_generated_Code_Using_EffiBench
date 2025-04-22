#1337 The K Weakest Rows In A Matrix
#https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/

import time
from typing import List
from bisect import bisect_right

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        
        # Count the number of 1s (soldiers) in each row
        # Since rows are sorted (1s followed by 0s), we reverse and use bisect_right on 0
        soldier_counts = [n - bisect_right(row[::-1], 0) for row in mat]

        # Create a list of indices for the rows
        row_indices = list(range(m))

        # Sort the indices based on the number of soldiers in each row
        row_indices.sort(key=lambda i: soldier_counts[i])

        # Return the indices of the k weakest rows
        return row_indices[:k]
test_cases = [
    ([[0, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 1, 0, 0], [1, 1], [1, 1, 1, 0, 1], [0, 1, 0], [1, 1, 1, 0, 0, 0, 0, 1, 1]], 1, [1]),
    ([[1, 0, 0, 1, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 0, 1, 1, 0, 1, 1], [1, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 1, 0], [1, 1, 1, 0, 0, 1, 0, 1, 1, 0], [0, 0, 1, 0, 1, 0, 0, 0, 1], [1, 1]], 3, [5, 1, 7]),
    ([[1, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 1, 1, 1, 0, 0], [0, 1, 1, 0], [0, 1, 1, 1]], 4, [2, 1, 0, 3]),
    ([[0, 0, 1, 0, 0, 1, 0], [1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 0, 0, 1], [1, 1, 0, 0, 1, 1, 0, 0]], 5, [4, 0, 5, 1, 3]),
    ([[1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0, 0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 0]], 5, [6, 1, 3, 0, 2]),
    ([[1, 0, 0, 1, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0], [1, 1, 1, 0], [1, 1], [1, 0, 1, 1, 1, 0, 0, 0, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1], [0, 1], [1, 0, 1, 1, 1, 0, 0, 0, 1]], 8, [1, 5, 6, 0, 8, 7, 2, 3]),
    ([[1, 1, 0], [0, 0, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1, 0, 1, 1, 0], [1, 0, 0, 1, 1, 0, 1, 0]], 6, [3, 8, 9, 1, 2, 4]),
    ([[0, 0, 0, 0, 1, 1, 0, 1, 0, 0], [1, 1, 1, 0, 1, 1]], 1, [0]),
    ([[1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 0, 0, 1, 0, 0], [1, 1, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1, 0, 0], [1, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 0]], 5, [3, 6, 1, 0, 5]),
    ([[0, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 1, 1, 0]], 1, [0])
]

sol = Solution()
total_time = 0.0

for mat, k, expected in test_cases:
    start_time = time.perf_counter()
    result = sol.kWeakestRows(mat, k)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    assert result == expected, f"Test failed for amt({mat}, {k}). Expected {expected}, got {result}"
    print(f"Test passed for mat={mat}, k={k}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds") 
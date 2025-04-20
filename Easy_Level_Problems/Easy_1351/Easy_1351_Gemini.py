#1351. Count Negative Numbers in a Sorted Matrix
#https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/


import time

from typing import List


class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        # Start from the top-right corner
        row, col = m - 1, 0
        count = 0
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                # If current element is negative, all elements below it are also negative
                count += n - col
                row -= 1  # Move up
            else:
                # If current element is non-negative, move right
                col += 1

        return count
    

solution = Solution()

# Test cases
test_cases = [
    ([[-41, -43, -91, -85, 59, -36, 9, -19, 68, -93, 39], [62, -82, -51, -55, 74, 92, 25, 32, 12, -88, -8], [15, -45, -2, 18, -95, 17, 60, 44, 99, -42, 32]], 30),
    ([[-54, 20, 19, 31, -20, 47, 1, 50, 46, 77], [-80, 22, 15, 75, -31, 25, -42, -22, -61, -75], [-27, -22, -3, -19, 2, -37, -24, 91, 4, -41]], 30),
    ([[-41, -23, -17, -18, 1, 46, 74, -35, -51, -65, -71], [-87, 84, -47, 18, -60, 9, 6, -34, -8, 48, 80], [85, 21, 88, -53, -35, 69, -85, 38, 5, -63, -56], [-90, 65, -35, 49, -84, 82, 3, 9, -47, -34, -3]], 30),
    ([[25, -6, -43, -2], [70, 55, 47, 12], [-11, 26, 5, -38], [-58, 31, 35, 9], [37, 46, 39, 82], [-60, 69, -74, -87], [-66, 79, -88, 41], [55, 67, 22, 80], [28, -65, -5, -10], [-75, -19, 0, -100]], 7),
    ([[40, -82, -77, 13], [-42, 91, 17, -68], [8, -80, -81, -92], [-3, 24, -96, 52], [-54, -45, 38, -96], [-47, 27, 95, -32], [-72, 83, -1, -70], [20, -89, -36, 87], [-74, 52, -39, 70]], 11),
    ([[44], [-21], [-24], [-66], [50], [-61], [-35], [-40], [-89], [-3]], 5),
    ([[16, 29, -79, 91, 45]], 3),
    ([[50, -44, -95, -79, 51, -73, -34, -45, -88], [25, 63, -58, -24, -89, 73, 37, 40, -15], [87, -16, 77, -63, -39, -51, -67, -60, -62], [52, -75, 46, -16, -91, -38, -89, -93, 78], [-20, 10, -13, 73, -48, 21, 52, 3, 65], [11, -43, -94, 42, -6, 96, 85, 11, 87], [1, 69, -54, -52, 46, -92, -70, 35, 33], [-64, -15, -43, 3, -64, 95, 20, 37, 94], [-4, 37, 29, 86, 82, 24, 4, -35, -5], [77, -36, 22, 14, 38, -96, 30, 89, -31], [73, 27, 96, -64, 54, 73, -75, -80, -60]], 12),
    ([[-30, -47, -62, 73, -2, -90, -38], [-46, -8, -27, -55, -38, -74, 23], [89, -35, -64, -22, -51, 5, 92], [-36, 21, -37, 63, -42, 26, -73], [42, 3, 85, 40, 78, 16, 79], [17, 3, -99, -23, -92, 96, 8], [-7, -58, 32, 85, -2, -1, 36], [85, -94, 52, 43, 38, 23, -84], [-31, 32, -71, -21, -82, 48, 27], [61, -83, 32, -11, 76, 55, 77], [82, 57, -23, 3, 2, -68, 7]], 14),
    ([[-44], [-97], [54]], 0)
]

# Measure performance
total_time = 0.0

for grid, expected in test_cases:
    start_time = time.perf_counter()
    result = solution.countNegatives(grid)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    
    # Check if test case passed
    assert result == expected, f"Test failed for grid={grid}. Expected {expected}, got {result}"
    print(f"Test passed for grid={grid}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")


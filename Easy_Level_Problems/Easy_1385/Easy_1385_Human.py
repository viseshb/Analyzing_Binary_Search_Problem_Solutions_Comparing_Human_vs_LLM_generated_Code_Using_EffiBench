#1385. Find the Distance Value Between Two Arrays
#https://leetcode.com/problems/find-the-distance-value-between-two-arrays/


import time


from typing import List
from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def check(a: int) -> bool:
            i = bisect_left(arr2, a - d)
            return i == len(arr2) or arr2[i] > a + d

        arr2.sort()
        return sum(check(a) for a in arr1)

sol = Solution()
# Test cases
test_cases = [
    
    ([71, 15, 2, 77], [29, 34, 37, 52, 61, 73], 41,0),
    ([51], [2, 14, 30, 32, 55, 67, 72, 76, 79], 13, 0),
    ([54, 98, 43, 85, 4, 89, 76, 26, 5, 64], [22, 27, 31, 33, 45], 74, 0),
    ([3, 78, 56, 74, 84, 63, 90], [7, 47, 48, 79, 83, 84, 85, 86, 88], 81, 0),
    ([58, 42, 86, 77, 55, 97, 74, 45, 87], [17, 27, 34], 28, 5),
    ([19, 75, 91, 33, 52, 28, 93], [18, 27, 40, 59, 77, 88, 93], 36, 0),
    ([78, 49], [8, 20, 23, 25, 37, 43, 62, 64, 89, 90], 62, 0),
    ([73, 46, 36, 79, 39, 21, 68, 22, 57, 78], [16, 18, 19, 24, 26, 41, 53, 68, 69, 99], 84, 0),
    ([27, 44, 55, 78, 65, 36, 93, 39, 94, 76], [40, 67], 39, 0),
    ([92, 8, 38, 49], [11, 34, 52, 58, 85, 95], 68, 0)
]

# Measure performance
total_time = 0.0

for arr1, arr2, d, expected in test_cases:
    start_time = time.perf_counter()
    result = sol.findTheDistanceValue(arr1, arr2, d)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    
    # Check if test case passed
    assert result == expected, f"Test failed for arr1={arr1}, arr2={arr2} and d={d}. Expected {expected}, got {result}"
    print(f"Test passed for arr1={arr1}, arr2 ={arr2} and d={d}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")
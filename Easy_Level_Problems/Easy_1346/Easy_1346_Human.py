#1346. Check If N and Its Double Exist
#https://leetcode.com/problems/check-if-n-and-its-double-exist/description/


import time

from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        m = {v: i for i, v in enumerate(arr)}
        for i, v in enumerate(arr):
            if v * 2 in m and m[v * 2] != i:
                return True
        return False

test_cases = [
    ([-937, 684, -76, -888, -360, 325, -514, 41, 118, -990], False),
    ([43, 978, -412, 674, 100, 528, 19, 78, -296, 325],  False),
    ([-641, 176, -788, -471, -815], False),
    ([-150, -858, 115, 666, -213, 518, 238], False),
    ([-136, 471],  False),
    ([-384, -677],  False),
    ([-647, 950, -501, 625, -682, 609, -237, -732, 842, 297],  False),
    ([302, 18, -90, 682, 48, 528, -59, 0],  False),
    ([-417, -444, 644],  False),
    ([-184, -338, -361, -84, -153, 493, 376, 887, -37], False)
]

sol = Solution()
total_time = 0.0

for arr, expected in test_cases:
    start_time = time.perf_counter()
    result = sol.checkIfExist(arr)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    assert result == expected, f"Test failed for arr({arr}). Expected {expected}, got {result}"
    print(f"Test passed for arr={arr}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds") 
#4. Median of Two Sorted Arrays
#https://leetcode.com/problems/median-of-two-sorted-arrays/description/

from cmath import inf
import time
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def f(i: int, j: int, k: int) -> int:
            if i >= m:
                return nums2[j + k - 1]
            if j >= n:
                return nums1[i + k - 1]
            if k == 1:
                return min(nums1[i], nums2[j])
            p = k // 2
            x = nums1[i + p - 1] if i + p - 1 < m else inf
            y = nums2[j + p - 1] if j + p - 1 < n else inf
            return f(i + p, j, k - p) if x < y else f(i, j + p, k - p)

        m, n = len(nums1), len(nums2)
        a = f(0, 0, (m + n + 1) // 2)
        b = f(0, 0, (m + n + 2) // 2)
        return (a + b) / 2



sol = Solution()

test_cases = [
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5),
    ([20, 67], [37, 85], 52.0),
    ([1, 2, 13, 22, 34, 46, 63, 86], [59, 80], 40.0),
    ([8, 57, 82, 87], [8, 18, 20, 23, 40, 41, 54, 63, 72, 93], 47.5),
    ([3, 36, 78], [13, 20, 28, 45, 59, 89], 36.0),
    ([17, 34, 43, 48, 51, 53, 83, 88], [43, 48, 54, 78, 88], 51.0),
    ([21, 28, 53, 63, 94], [6, 9, 25, 27, 31, 55, 60, 67, 78], 42.0),
    ([17, 50, 54], [1, 20, 46, 52, 53, 62, 63, 66, 70], 52.5),
    ([11, 13, 15, 27, 29, 55, 74, 89, 96], [9, 39, 72], 34.0)
]
total_time = 0.0
result = None

for nums1, nums2, expected in test_cases:
    start_time = time.perf_counter()
    result = sol.findMedianSortedArrays(nums1, nums2)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    assert result == expected, f"Test failed for nums1={nums1}, nums2={nums2}. Expected {expected}, got {result}"
    print(f"Test passed for nums1={nums1}, nums2={nums2}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")

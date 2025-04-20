#350. Intersection of Two Arrays II
#https://leetcode.com/problems/intersection-of-two-arrays-ii/


import time
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        ptr1, ptr2 = 0, 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] == nums2[ptr2]:
                result.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1
        return result

solution = Solution()

# Test cases
test_cases = [
    ([5, 13, 59, 82, 92, 43], [32, 30, 60, 90, 49, 16, 43, 85, 55],[43]),
    ([86, 90], [53, 59, 7, 68, 16, 48, 35, 14, 56],[]),
    ([37, 61, 94, 87, 6, 40], [26, 87, 48, 72, 81, 74],[87]),
    ([17, 65], [3, 48],[]),
    ([31, 27, 16, 2, 53, 12], [41, 50, 44, 37, 91, 85, 84, 43],[]),
    ([68, 93, 96, 49, 58, 27, 39], [6, 71, 95, 21, 18, 85, 22, 20, 75],[]),
    ([11, 52, 75, 59, 86], [53, 12, 35],[]),
    ([30, 50], [15, 97, 81, 30],[30]),
    ([10, 53, 21, 96, 42], [46, 52, 34],[]),
    ([6, 40, 56, 14, 68, 49, 7], [86, 52, 84, 72, 31, 16, 5, 37],[])
]

# Measure performance
total_time = 0.0

for nums1, nums2, expected in test_cases:
    start_time = time.perf_counter()
    result = solution.intersect(nums1, nums2)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    
    # Check if test case passed
    assert result == expected, f"Test failed for nums1={nums1}, nums2={nums2}. Expected {expected}, got {result}"
    print(f"Test passed for nums1={nums1}, nums2={nums2}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")
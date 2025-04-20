#349. Intersection of Two Arrays
#https://leetcode.com/problems/intersection-of-two-arrays/description/

import time
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        result = set()
        for num1 in nums1:
            left, right = 0, len(nums2) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums2[mid] == num1:
                    result.add(num1)
                    break
                elif nums2[mid] < num1:
                    left = mid + 1
                else:
                    right = mid - 1
        return list(result)
       
solution = Solution()

# Test cases
test_cases = [
    ([990, 57, 86, 782, 177, 325, 976, 383, 131], [661, 277, 246, 423, 259, 358, 947, 86, 404],[86]),
    ([459, 993, 350, 631], [756, 169, 617, 599, 672, 504, 350],[350] ),
    ([233, 209, 870, 368, 429, 997, 33, 19], [33, 587, 45, 711],[33]),
    ([442, 159, 917, 580, 144, 705, 525, 172, 18, 547], [426, 525, 514, 973, 9, 254, 444],[525]),
    ([105, 448], [129, 281, 448, 182],[448])
    
]

# Measure performance
total_time = 0.0

for nums1, nums2, expected in test_cases:
    start_time = time.perf_counter()
    result = solution.intersection(nums1, nums2)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    
    # Check if test case passed
    assert result == expected, f"Test failed for nums1={nums1}, nums2={nums2}. Expected {expected}, got {result}"
    print(f"Test passed for nums1={nums1}, nums2={nums2}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")
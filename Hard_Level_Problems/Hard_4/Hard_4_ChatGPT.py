# #4. Median of Two Sorted Arrays
# #https://leetcode.com/problems/median-of-two-sorted-arrays/description/
          
from typing import List
import time

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        imin, imax = 0, m
        half_len = (m + n + 1) // 2
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1  # i is too small
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1  # i is too big
            else:
                # i is perfect
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0

# Create an instance of the Solution class
solution = Solution()

# Test cases
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

# Measure performance
total_time = 0.0

for nums1, nums2, expected in test_cases:
    start_time = time.perf_counter()
    result = solution.findMedianSortedArrays(nums1, nums2)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    
    # Check if test case passed
    assert result == expected, f"Test failed for nums1={nums1}, nums2={nums2}. Expected {expected}, got {result}"
    print(f"Test passed for nums1={nums1}, nums2={nums2}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")

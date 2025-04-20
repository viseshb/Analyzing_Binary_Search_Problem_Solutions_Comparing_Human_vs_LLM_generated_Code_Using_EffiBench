#162. Find Peak Element
#https://leetcode.com/problems/find-peak-element/
import time
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is less than its right neighbor,
            # a peak must exist in the right half (including the neighbor)
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # If the middle element is greater than its right neighbor,
            # a peak must exist in the left half (including the middle element)
            else:
                right = mid
        
        # When left == right, we've found a peak element
        return left

# Define test cases: List of tuples (input_list, expected_peak_index)
test_cases = [
    ([11, 22, 35], 2),
    ([88, 84, 81, 57, 83, 96, 40, 80, 9], 7),
    ([57, 90, 85, 45, 51, 73], 1),
    ([100, 2, 40, 24, 8, 52, 64, 47, 80], 6),
    ([8, 66, 87, 23, 75, 19], 2),
    ([14, 95, 70, 13, 51, 35, 49, 59], 7),
    ([17, 63, 83, 9, 88, 21], 2),
    ([51, 48, 8, 31, 56, 10], 4),
    ([52, 87, 69, 59, 22, 38, 24, 47], 1),
    ([39, 16, 77, 93, 41, 91], 5)
]

solution = Solution()
total_time = 0.0

for idx, (nums, expected) in enumerate(test_cases, 1):
    start_time = time.perf_counter()
    result = solution.findPeakElement(nums)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time

    assert result == expected, f"Test failed for nums={nums}. Expected {expected}, got {result}"
    print(f"Test {idx} passed for nums={nums}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")

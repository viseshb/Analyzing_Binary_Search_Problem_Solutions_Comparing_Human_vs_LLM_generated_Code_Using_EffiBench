#350. Intersection of Two Arrays II
#https://leetcode.com/problems/intersection-of-two-arrays-ii/


import time
from typing import List

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Sort the arrays
        nums1.sort()
        nums2.sort()
        
        # Choose the smaller array for binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        result = []
        # Make a copy of nums2 that we can modify
        search_array = nums2.copy()
        
        for num in nums1:
            # Use binary search to find the index of num in search_array
            index = self.binary_search(search_array, num)
            
            # If found, add to result and remove from search_array
            if index != -1:
                result.append(num)
                search_array.pop(index)
        
        return result
    
    def binary_search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1

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
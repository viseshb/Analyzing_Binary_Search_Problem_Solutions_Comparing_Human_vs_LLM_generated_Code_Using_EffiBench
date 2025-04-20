#349. Intersection of Two Arrays
#https://leetcode.com/problems/intersection-of-two-arrays/description/


import time
from typing import List

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Sort the second array to perform binary search on it
        nums2.sort()
        
        # Use a set to store unique elements from the intersection
        result = set()
        
        # Iterate through each element in nums1
        for num in nums1:
            # If we already found this number, skip
            if num in result:
                continue
            
            # Perform binary search on nums2
            if self.binary_search(nums2, num):
                result.add(num)
        
        # Convert set to list for return
        return list(result)
    
    def binary_search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
          
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
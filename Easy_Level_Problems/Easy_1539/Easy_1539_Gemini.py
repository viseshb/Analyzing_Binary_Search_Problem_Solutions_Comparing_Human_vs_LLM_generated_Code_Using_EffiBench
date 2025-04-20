#1539. Kth Missing Positive Number
#https://leetcode.com/problems/kth-missing-positive-number/

import time
from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0
        current = 1
        arr_index = 0
        while missing_count < k:
            if arr_index < len(arr) and arr[arr_index] == current:
                arr_index += 1
            else:
                missing_count += 1
                if missing_count == k:
                    return current
            current += 1
        return current - 1
    
sol = Solution()
# Test cases
test_cases = [
    
    ([80, 114, 249, 442, 555, 644, 665, 747, 869], 494, 498),
    ([321, 329, 384, 431, 443, 580], 977, 983),
    ([86, 163, 342, 351, 583, 704, 713, 739, 876, 906], 139, 140),
    ([6, 163, 191, 298, 355, 811, 830, 905, 919], 739, 744),
    ([760, 837, 934, 949], 605, 605),
    ([989], 189, 189),
    ([53], 472, 473),
    ([67, 152, 240, 299, 417, 520, 650, 717, 740], 499, 504),
    ([337, 384, 456, 557], 419, 421),
    ([10, 54, 257, 424, 700, 904, 931], 466, 470)
]

# Measure performance
total_time = 0.0

for arr, k, expected in test_cases:
    start_time = time.perf_counter()
    result = sol.findKthPositive(arr, k)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    
    # Check if test case passed 
    assert result == expected, f"Test failed for arr={arr}, k= {k}. Expected {expected}, got {result}"
    print(f"Test passed for arr={arr} and k = {k}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")   

#69. Sqrt(x)
#https://leetcode.com/problems/sqrtx/

import time

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = (left + right + 1) >> 1
            if mid <= x // mid:
                left = mid
            else:
                right = mid - 1
        return left


solution = Solution()

# Test cases
test_cases = [
    (1183590127, 34403),
    (614217718,24783),
    (250407520,15824),
    (1168930359,34189),
    (1611111290,40138),
    (1350239661,36745),
    (1628456674,40354),
    (1992105920,44633),
    (2136663874,46224),
    (1088576031,32993),
    

]

# Measure performance
total_time = 0.0

for x, expected in test_cases:
    start_time = time.perf_counter()
    result = solution.mySqrt(x)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    
    # Check if test case passed
    assert result == expected, f"Test failed for nums1={x}. Expected {expected}, got {result}"
    print(f"Test passed for nums1={x}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")

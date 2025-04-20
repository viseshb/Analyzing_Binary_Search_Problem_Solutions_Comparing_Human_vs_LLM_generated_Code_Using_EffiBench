#69. Sqrt(x)
#https://leetcode.com/problems/sqrtx/

import time
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left, right = 1, x
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # If mid*mid == x, we found the exact square root
            if mid * mid == x:
                return mid
            
            # If mid*mid > x, search in the left half
            elif mid * mid > x:
                right = mid - 1
            
            # If mid*mid < x, search in the right half
            else:
                left = mid + 1
        
        # When we exit the loop, right is the integer square root of x
        # (rounded down, as required)
        return right

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

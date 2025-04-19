#668. Kth Smallest Number in Multiplication Table
#https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

import time

class Solution:
    def findKthNumber(self, m, n, k):
        # Use binary search to find the kth smallest number
        left, right = 1, m * n
        
        while left < right:
            mid = left + (right - left) // 2
            count = self.count_less_or_equal(mid, m, n)
            
            if count < k:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    def count_less_or_equal(self, target, m, n):
        # Count numbers less than or equal to target in the multiplication table
        count = 0
        for i in range(1, m + 1):
            # For each row, count how many numbers are <= target
            count += min(target // i, n)
        return count
    

test_cases = [
    (802, 488, 222929 ,90774),
    (353, 193, 15020, 3978),
    (427, 932, 63865, 15105),
    (437, 333, 108367, 55094),
    (608, 993, 89762, 20704),
    (418, 394, 93913, 38346),
    (324, 308, 98762, 86100),
    (44, 552, 547, 130),
    (291, 434, 105147, 60916),
    (701, 539, 53259, 12138)
]

sol = Solution()
total_time = 0.0

for m, n, k, expected in test_cases:
    start_time = time.perf_counter()
    result = sol.findKthNumber(m,n,k)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    assert result == expected, f"Test failed for nums({m}, {n}, {k}). Expected {expected}, got {result}"
    print(f"Test passed for nums=({m}, {n}, {k}). Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")
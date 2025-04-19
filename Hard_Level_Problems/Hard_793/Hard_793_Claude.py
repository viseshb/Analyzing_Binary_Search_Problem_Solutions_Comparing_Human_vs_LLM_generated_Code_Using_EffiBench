#793. Preimage Size of Factorial Zeroes Function
#https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

import time
class Solution:
    def preimageSizeFZF(self, k):
        # Function to count trailing zeros in n!
        def trailingZeros(n):
            count = 0
            divisor = 5
            while divisor <= n:
                count += n // divisor
                divisor *= 5
            return count
        
        # Binary search to find the smallest number with at least k trailing zeros
        def search(k):
            left, right = 0, 5 * k + 1  # Upper bound is sufficient
            
            while left < right:
                mid = (left + right) // 2
                zeros = trailingZeros(mid)
                
                if zeros < k:
                    left = mid + 1
                else:
                    right = mid
            
            return left
        
        # Find first number with k trailing zeros and first with k+1 trailing zeros
        first_with_k = search(k)
        first_with_k_plus_1 = search(k + 1)
        
        # Count of numbers with exactly k trailing zeros
        return first_with_k_plus_1 - first_with_k
    

test_cases = [
    (51, 5),
    (100, 5),
    (84, 5),
    (62, 5),
    (73, 0),
    (76, 5),
    (27, 5),
    (51, 5),
    (85, 0),
    (38, 5),
]


sol = Solution()
total_time = 0.0

for k, expected in test_cases:
    start_time = time.perf_counter()
    result = sol.preimageSizeFZF(k)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    assert result == expected, f"Test failed for k({k}). Expected {expected}, got {result}"
    print(f"Test passed for k=({k}). Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")  
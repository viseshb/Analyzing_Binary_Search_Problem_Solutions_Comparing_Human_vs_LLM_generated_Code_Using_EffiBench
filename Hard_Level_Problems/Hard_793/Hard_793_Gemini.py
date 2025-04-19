#793. Preimage Size of Factorial Zeroes Function
#https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/


import time
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def trailingZeroes(n):
            count = 0
            while n > 0:
                n //= 5
                count += n
            return count

        def find_bound(target):
            left, right = 0, 5 * (target + 1)
            while left < right:
                mid = (left + right) // 2
                if trailingZeroes(mid) < target + 1:
                    left = mid + 1
                else:
                    right = mid
            return left

        upper = find_bound(k)
        lower = find_bound(k - 1)
        return upper - lower
    
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

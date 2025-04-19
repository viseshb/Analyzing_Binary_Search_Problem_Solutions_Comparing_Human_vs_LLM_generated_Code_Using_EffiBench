#793. Preimage Size of Factorial Zeroes Function
#https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/


from bisect import bisect_left
import time

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def f(x):
            if x == 0:
                return 0
            return x // 5 + f(x // 5)

        def g(k):
            return bisect_left(range(5 * k), k, key=f)

        return g(k + 1) - g(k)

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
   

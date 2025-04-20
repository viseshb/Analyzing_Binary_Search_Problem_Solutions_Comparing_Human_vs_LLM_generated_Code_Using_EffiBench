#367. Valid Perfect Square
#https://leetcode.com/problems/valid-perfect-square/

import time

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left, right = 2, num // 2
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

test_cases = [
    (198794985, False),
    (720548389, False),
    (250143627, False),
    (365152663, False),
    (538451209, False),
    (115641585, False),
    (959452724, False),
    (479537366, False),
    (744827671, False),
    (944380383, False)
]

sol = Solution()
total_time = 0.0

for num, expected in test_cases:
    start_time = time.perf_counter()
    result = sol.isPerfectSquare(num)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    assert result == expected, f"Test failed for num({num}). Expected {expected}, got {result}"
    print(f"Test passed for num={num}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds") 

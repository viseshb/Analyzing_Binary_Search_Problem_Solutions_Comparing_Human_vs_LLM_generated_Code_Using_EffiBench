#400. Nth Digit
#https://leetcode.com/problems/nth-digit/
import time

class Solution:
    def findNthDigit(self, n: int) -> int:
        k, cnt = 1, 9  # Start with 1-digit numbers (1 to 9)
        
        # Determine the range of digits that includes the nth digit
        while n > k * cnt:
            n -= k * cnt  # Reduce n by the number of digits in the current range
            k += 1  # Move to the next range (2-digit, 3-digit, etc.)
            cnt *= 10  # The number of elements in the range increases (9, 90, 900, ...)
        
        # Now, n is within the range of k-digit numbers.
        # Find the number where the nth digit is located
        num = 10 ** (k - 1) + (n - 1) // k
        
        # Find the index of the digit within the number
        idx = (n - 1) % k
        
        # Return the specific digit
        return int(str(num)[idx])


testcases = [
    (46, 2),
    (26, 1),
    (79, 4),
    (36, 2),
    (60, 3),
    (58, 3),
    (12, 1),
    (60, 3),
    (93, 1),
    (98, 5)
]

solution = Solution()
total_time = 0.0

for idx, (nums, expected) in enumerate(testcases, 1):
    start_time = time.perf_counter()
    result = solution.findNthDigit(nums)  # Correct function call
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time

    assert result == expected, f"Test failed for nums={nums}. Expected {expected}, got {result}"
    print(f"Test {idx} passed for nums={nums}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")

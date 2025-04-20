#400. Nth Digit
#https://leetcode.com/problems/nth-digit/
import time
class Solution:
    def findNthDigitBinarySearch(self, n: int) -> int:
        def count_digits(k):
            """Calculates the total number of digits in numbers from 1 to k."""
            count = 0
            length = 1
            power_of_10 = 1
            while power_of_10 <= k:
                upper_bound = min(k, power_of_10 * 10 - 1)
                count += (upper_bound - power_of_10 + 1) * length
                if power_of_10 > k // 10:  # Avoid overflow
                    break
                power_of_10 *= 10
                length += 1
            return count

        low = 1
        high = 2 * n  # A reasonable upper bound (can be tighter)

        # Binary search to find the number containing the nth digit
        while low <= high:
            mid = (low + high) // 2
            if count_digits(mid) >= n:
                potential_number = mid
                high = mid - 1
            else:
                low = mid + 1

        # Once we have the potential number, we need to find the exact digit
        digits_before = count_digits(potential_number - 1)
        remaining_digits = n - digits_before
        index_in_number = remaining_digits - 1

        return int(str(potential_number)[index_in_number])

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
    result = solution.findNthDigitBinarySearch(nums)  # Correct function call
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time

    assert result == expected, f"Test failed for nums={nums}. Expected {expected}, got {result}"
    print(f"Test {idx} passed for nums={nums}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")

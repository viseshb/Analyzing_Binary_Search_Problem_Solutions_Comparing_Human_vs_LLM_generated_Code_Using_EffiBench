import time

class Solution:
    def findNthDigit(self, n: int) -> int:
        # Helper function to calculate the number of digits in a range of numbers with d digits
        def digits_count(d):
            return d * 9 * 10 ** (d - 1)

        # Step 1: Find how many digits the number has
        left, right = 1, 10
        while left < right:
            mid = (left + right) // 2
            total = sum(digits_count(i) for i in range(1, mid + 1))
            if total < n:
                left = mid + 1
            else:
                right = mid

        # Find the length of the number and the previous digits count
        digit_length = left
        prev_digits = sum(digits_count(i) for i in range(1, digit_length))
        
        # Find the specific digit within the number range
        index = n - prev_digits - 1
        start = 10 ** (digit_length - 1)
        number = start + index // digit_length
        
        # Return the specific digit in the number
        return int(str(number)[index % digit_length])

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

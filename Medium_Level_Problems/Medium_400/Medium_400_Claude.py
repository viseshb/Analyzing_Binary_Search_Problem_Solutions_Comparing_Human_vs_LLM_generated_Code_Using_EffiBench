import time

class Solution:
    def findNthDigit(self, n: int) -> int:
        # Step 1: Determine the length of the number that contains the nth digit
        start = 1  # Starting digit
        digit_length = 1  # Length of numbers we're considering
        count = 9  # Count of numbers with current digit_length
        
        # Find the length of the number that contains the nth digit
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10
        
        # Step 2: Find the actual number that contains the nth digit
        # We've reduced n to be the position within numbers of digit_length length
        number = start + (n - 1) // digit_length
        
        # Step 3: Find the digit within this number
        position = (n - 1) % digit_length  # 0-indexed position from the left
        
        # Convert number to string to easily get the digit
        return int(str(number)[position])


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

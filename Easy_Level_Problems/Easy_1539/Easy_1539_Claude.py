#1539. Kth Missing Positive Number
#https://leetcode.com/problems/kth-missing-positive-number/
import time
class Solution:
   def findKthPositive(self, arr: list[int], k: int) -> int:
       # Initialize the pointer to the first element of the array
       # and a counter for missing numbers
       current_expected = 1
       missing_count = 0
       
       # Loop through the array
       for num in arr:
           # Count how many numbers are missing between the previous and current element
           missing_count += num - current_expected
           
           # If we've found k or more missing numbers, calculate the kth missing number
           if missing_count >= k:
               # Go back to the last number before we exceeded k missing numbers
               return num - (missing_count - k + 1)
           
           # Update current_expected to the next number we expect to see
           current_expected = num + 1
       
       # If we've gone through the entire array and still haven't found k missing numbers,
       # the kth missing number is after the last element of the array
       return arr[-1] + (k - missing_count)
sol = Solution()
# Test cases
test_cases = [
    
    ([80, 114, 249, 442, 555, 644, 665, 747, 869], 494, 498),
    ([321, 329, 384, 431, 443, 580], 977, 983),
    ([86, 163, 342, 351, 583, 704, 713, 739, 876, 906], 139, 140),
    ([6, 163, 191, 298, 355, 811, 830, 905, 919], 739, 744),
    ([760, 837, 934, 949], 605, 605),
    ([989], 189, 189),
    ([53], 472, 473),
    ([67, 152, 240, 299, 417, 520, 650, 717, 740], 499, 504),
    ([337, 384, 456, 557], 419, 421),
    ([10, 54, 257, 424, 700, 904, 931], 466, 470)
]

# Measure performance
total_time = 0.0

for arr, k, expected in test_cases:
    start_time = time.perf_counter()
    result = sol.findKthPositive(arr, k)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    
    # Check if test case passed 
    assert result == expected, f"Test failed for arr={arr}, k= {k}. Expected {expected}, got {result}"
    print(f"Test passed for arr={arr} and k = {k}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")   
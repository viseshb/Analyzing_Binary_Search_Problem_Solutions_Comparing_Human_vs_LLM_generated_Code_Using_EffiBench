#410. Split Array Largest Sum
#https://leetcode.com/problems/split-array-largest-sum/description/

import time

class Solution:
    def splitArray(self, nums, k):
        # Helper function to check if we can split the array into k or fewer subarrays
        # such that each subarray has a sum less than or equal to mid
        def canSplit(mid):
            count = 1
            current_sum = 0
            
            for num in nums:
                current_sum += num
                if current_sum > mid:
                    count += 1
                    current_sum = num
                    if count > k:
                        return False
            
            return True
        
        # Binary search to find the minimum possible largest subarray sum
        left = max(nums)  # Minimum possible value is the max element
        right = sum(nums)  # Maximum possible value is the sum of all elements
        
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
    
test_cases = [
    ([681, 630, 94, 58, 88, 835, 727, 989], 5, 989),
    ([313, 711, 755, 856, 593], 1,3228),
    ([893, 865, 255, 469, 370, 566], 2, 1758),
    ([934, 53, 66, 283, 149, 401], 6, 934),
    ([21, 469, 787, 734, 19, 401, 639, 484], 8, 787),
    ([892, 492, 306, 699, 16, 43, 602, 42, 925, 861], 7, 925),
    ([181], 1 ,181 ),
    ([763, 487, 674, 284, 566, 807, 371, 68], 1, 4020),
    ([242, 329, 439, 127, 42, 331, 816], 1, 2326),
    ([711, 681, 355, 37, 476, 753], 1, 3013)
]

sol = Solution()
total_time = 0.0

for nums, k, expected in test_cases:
    start_time = time.perf_counter()
    result = sol.splitArray(nums, k)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    assert result == expected, f"Test failed for nums({nums}, {k}). Expected {expected}, got {result}"
    print(f"Test passed for nums={nums}, k={k}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")    
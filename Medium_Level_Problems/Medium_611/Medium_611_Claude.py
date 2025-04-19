import time

from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Sort the array to make it easier to find valid triangles
        nums.sort()
        n = len(nums)
        count = 0
        
        # For a valid triangle, the sum of any two sides must be greater than the third side
        # Since we've sorted the array, we only need to check if nums[i] + nums[j] > nums[k]
        # where i < j < k
        
        # Fix the largest side (k) and find pairs (i,j) that can form a triangle with it
        for k in range(2, n):
            i = 0
            j = k - 1
            while i < j:
                # If nums[i] + nums[j] > nums[k], then all elements between i and j
                # can also form triangles with nums[k]
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    # If the sum is not greater, we need a larger first element
                    i += 1
                    
        return count
    
testcases = [
    ([305, 405, 432, 770, 844], 5),
    ([39, 41, 110, 114, 204, 206, 236, 266, 311, 390, 561, 563, 618, 712, 781, 807, 856, 896, 920, 996], 423),
    ([112, 225, 231, 270, 304, 357, 371, 462, 468, 578, 593, 656, 772, 842, 886], 269),
    ([16, 82, 144, 164, 252, 316, 453, 490, 512, 569, 614, 635, 638, 684, 806, 929], 266),
    ([2, 28, 141, 249, 280, 400, 511, 783, 985], 13),
    ([116, 440, 769, 928, 959], 5),
    ([61, 394, 455, 609, 839], 4),
    ([82, 138, 210, 534, 596, 625, 628, 644, 706, 734, 774, 779, 979], 198),
    ([48, 158, 297, 369, 583, 670, 710, 729, 758, 786, 831], 101),
    ([32, 154, 214, 222, 258, 390, 539, 779, 837, 861, 918, 940, 964, 993], 178)
]

solution = Solution()
total_time = 0.0

for idx, (nums, expected) in enumerate(testcases, 1):  # Fixed variable name to nums
    start_time = time.perf_counter()
    result = solution.triangleNumber(nums)  # Correct function call
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time

    assert result == expected, f"Test failed for test case {idx}. Expected {expected}, got {result}"
    print(f"Test {idx} passed. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")

from typing import List
import time

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

# Initialize the solution instance
solution = Solution()

test_cases = [
    ([-9291, -1385], 7240, False),
    ([-8954, -8049, -7190, -2609, -382, 609, 5612, 6601, 8155], -8472, False),
    ([-6379, -4501, -1283, 325, 5728, 5823, 7194, 7221], -7012, False),
    ([-8672, -6987, -1908, 312, 658, 3573, 4770], -2400, False),
    ([-9641, -4751, -3099, -1804, -1255, 2287, 4166], -3608, False),
    ([-5954, -2108, 5357, 5443], -7450, False),
    ([-8637, -8052, -4351, -2411, -1809, 986, 3731, 6794], -3397, False),
    ([-9793, -1351, -252, 3068, 4484], 1923, False),
    ([-8044, -6003, -3837, -1905, 1596, 4310, 4810, 7633, 8151], -8753, False),
    ([-7230, -3044, -1756, 1047, 7140], 6685, False),
    ([2, 5, 6, 0, 0, 1, 2], 0, True)
]

total_time = 0.0

for nums, target, expected in test_cases:
    start_time = time.perf_counter()
    search_result = solution.search(nums, target)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    assert search_result == expected, f"Test failed for nums={nums}, target={target}. Expected {expected}, got {search_result}"
    print(f"Test passed for nums={nums}, target={target}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")

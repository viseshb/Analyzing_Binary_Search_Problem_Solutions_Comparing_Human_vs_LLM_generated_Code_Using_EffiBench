import time

class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        max_len = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_len

testcases = [
    ([26, 31, 73, 80], [66, 23, 60, 49, 40, 21, 26], 1),
    ([8, 34, 87, 6, 76, 1, 83, 77, 69, 39], [15, 93, 24, 81, 72], 0),
    ([33, 86, 52, 21], [30, 48, 92, 10, 68, 38, 91], 0),
    ([35, 16, 36, 55], [25, 23, 77], 0),
    ([93, 31, 80], [14, 84, 57, 62, 43, 95, 36], 0),
    ([50, 41, 45, 95, 63], [59, 20, 48, 55, 62, 72, 82, 96, 53, 91], 0),
    ([78, 9, 67, 20, 25], [89, 27, 97, 61, 31], 0),
    ([16, 4, 86, 12, 53, 66, 18, 95, 30], [87, 66, 18], 2),
    ([26, 57, 14, 91, 53, 75, 22, 31, 98, 82, 99], [75, 17, 26, 43, 50, 54], 1),
    ([13, 61, 76, 95, 25], [88, 61, 54, 78, 2, 48, 96, 7], 1)
]

solution = Solution()
total_time = 0.0

for idx, (nums1, nums2, expected) in enumerate(testcases, 1):  # Fixed to use nums1 and nums2
    start_time = time.perf_counter()
    result = solution.findLength(nums1, nums2)  # Correct function call with both arguments
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time

    assert result == expected, f"Test failed for test case {idx}. Expected {expected}, got {result}"
    print(f"Test {idx} passed. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")

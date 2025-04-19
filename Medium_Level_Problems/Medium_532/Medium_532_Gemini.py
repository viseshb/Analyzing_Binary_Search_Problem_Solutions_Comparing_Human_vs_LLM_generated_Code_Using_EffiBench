import time

class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        count = 0
        seen = set()
        if k < 0:
            return 0
        elif k == 0:
            freq = {}
            for num in nums:
                freq[num] = freq.get(num, 0) + 1
            for num, c in freq.items():
                if c >= 2:
                    count += 1
        else:
            nums_set = set(nums)
            for num in nums_set:
                if num + k in nums_set:
                    count += 1
        return count
    
testcases = [
    ([-6074712, 52689, -901992, -4396430], 1705633, 0),
    ([-7446539, -6003675], 5506152, 0),
    ([-6155247, 4506036, 8633870, -5932916, -8963834, -948378, -7971882, -4977975, 3110710, 7861664], 1010142, 0),
    ([8596762, -6393025, 1328286, 2595532, 5608206, 9263912, -409355, 7743506, 2800252, -1902766], 6348129, 0),
    ([-5782104, -9248023, -3896974, -535446], 2821537, 0),
    ([-8689283, -7747736, 330510, -2325823, 2348208, 2083531, -2452106], 4471450, 0),
    ([1963317, -6143468, -156092], 573175, 0),
    ([-4790543, 3399983], 6554933, 0),
    ([-656553, 9894876, -4009638], 3446381, 0),
    ([-877588, 8128335, 4793082, -253005, 2956841, -3308627, 6846413, 2225359, -3497176], 1795597, 0),
]

solution = Solution()
total_time = 0.0

for idx, (houses, heaters, expected) in enumerate(testcases, 1):
    start_time = time.perf_counter()
    result = solution.findPairs(houses, heaters)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time

    assert result == expected, f"Test failed for test case {idx}. Expected {expected}, got {result}"
    print(f"Test {idx} passed. Execution time: {execution_time:.12f} seconds")


print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")

#888. Fair Candy Swap
#https://leetcode.com/problems/fair-candy-swap/
import time


from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        diff = (sum_alice - sum_bob) // 2
        set_bob = set(bobSizes)

        for x in aliceSizes:
            target = x - diff
            if target in set_bob:
                return [x, target]
        return None
    
test_cases = [
    ([22, 18, 76, 82, 16, 10], [23, 40, 91, 53, 16, 93, 98], None),
    ([52, 6, 15, 7, 39, 29, 80], [48, 92, 96, 50, 77, 26, 99],  None),
    ([13, 68, 47, 69, 29, 96, 90, 34, 45], [100, 58, 94, 52, 27, 97], None),
    ([15, 88, 29, 33, 100, 53, 21], [26, 7, 32, 43, 93, 65, 35, 73, 42, 20], None),
    ([9, 35, 77, 14, 74, 97, 79], [42, 86, 87, 10, 96, 24, 3, 71, 83, 56], [9, 96]),
    ([40, 78, 66, 95, 37, 30], [94, 49, 8, 88, 79, 11, 61, 45, 89, 9], None),
    ([45, 33, 81, 4], [15, 92, 48], None),
    ([64, 11, 42, 79, 23, 17, 47, 5, 49, 90], [2, 4, 61, 71], None),
    ([31, 87, 37, 41, 88], [91, 64, 38, 84, 81, 11, 92, 24, 82, 66], None),
    ([17, 32, 98, 49, 15], [45, 65, 10, 20, 97], [32, 45])
]

sol = Solution()
total_time = 0.0

for aliceSizes, bobSizes, expected in test_cases:
    start_time = time.perf_counter()
    result = sol.fairCandySwap(aliceSizes, bobSizes)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    assert result == expected, f"Test failed for aliceSizes({aliceSizes}) and bobSizes{bobSizes}. Expected {expected}, got {result}"
    print(f"Test passed for aliceSizes={aliceSizes} and bobSizes= {bobSizes}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds") 

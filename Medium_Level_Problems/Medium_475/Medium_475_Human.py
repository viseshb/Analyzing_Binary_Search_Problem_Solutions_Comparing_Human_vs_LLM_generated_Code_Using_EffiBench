#475. Heaters
#https://leetcode.com/problems/heaters/
import time
from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Sort the houses and heaters
        houses.sort()
        heaters.sort()

        def check(r: int) -> bool:
            # Check if a given radius 'r' is sufficient
            m, n = len(houses), len(heaters)
            i, j = 0, 0
            while i < m:
                # Ensure the heater covers the house within the radius
                if j >= n:
                    return False
                mi = heaters[j] - r  # minimum position that heater[j] can cover
                mx = heaters[j] + r  # maximum position that heater[j] can cover
                if houses[i] < mi:
                    return False
                if houses[i] > mx:
                    # Move to the next heater if the current heater can't cover this house
                    j += 1
                else:
                    # The house is within the range of the current heater, move to the next house
                    i += 1
            return True

        # Binary search to find the minimum radius
        left, right = 0, int(1e9)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid  # Try smaller radius
            else:
                left = mid + 1  # Increase radius
        
        return left

testcases = [
    ([6, 23, 27, 43, 53, 91], [6, 14, 17, 19, 64, 66, 80, 83, 87, 99], 21),
    ([11, 21, 26, 28, 45, 85, 92], [67, 68], 56),
    ([5, 17, 82, 83], [3, 25, 33, 93, 100], 11),
    ([13, 23, 58, 67], [2, 42, 44, 47, 93, 95], 20),
    ([7, 18, 21, 22, 25, 75, 99], [7, 32, 42, 59, 96], 16),
    ([2, 10, 11, 15, 43, 66, 67, 79, 88, 100], [6, 28, 37, 42, 50, 54, 63, 90, 99], 11),
    ([11, 13, 17, 27, 55, 68, 77, 79, 82, 93], [9, 29, 36, 40, 41, 48, 61, 62, 78], 15),
    ([9, 60, 80, 95], [3, 6, 25, 37, 56, 72, 85, 88, 94], 5),
    ([6, 7, 8, 27, 50, 66, 73, 93], [2, 18, 36, 49, 57, 59, 75, 81], 12),
    ([1, 4, 18, 22, 50, 70, 79, 82, 92, 98], [6, 9, 11, 23, 27, 28, 44, 51, 70], 28)
]

solution = Solution()
total_time = 0.0

for idx, (houses, heaters, expected) in enumerate(testcases, 1):
    start_time = time.perf_counter()
    result = solution.findRadius(houses, heaters)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time

    assert result == expected, f"Test failed for test case {idx}. Expected {expected}, got {result}"
    print(f"Test {idx} passed. Execution time: {execution_time:.12f} seconds")


print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")

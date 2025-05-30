#354. Russian Doll Envelopes
#https://leetcode.com/problems/russian-doll-envelopes/description/

from typing import List
import time 
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def binary_search(dp: List[int], target: int) -> int:
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high) // 2
                if dp[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low  # the first index where dp[i] >= target

        # Sort by width ascending and height descending
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Extract only heights
        heights = [h for _, h in envelopes]

        dp = []
        for h in heights:
            idx = binary_search(dp, h)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h
        return len(dp)


test_cases = [
    (
        [[1, 44], [7, 55], [7, 35], [10, 59], [10, 40], [11, 66], [14, 30], [15, 77], [15, 71], [23, 59],
         [26, 58], [35, 48], [38, 86], [45, 21], [52, 90], [52, 86], [52, 77], [54, 95], [55, 60], [55, 44],
         [58, 56], [58, 16], [60, 76], [60, 50], [62, 96], [62, 81], [64, 27], [65, 76], [65, 26], [74, 16],
         [80, 39], [80, 15], [81, 38], [81, 34], [85, 99], [86, 34], [89, 39], [91, 2], [97, 91], [98, 94],
         [98, 68], [98, 64], [98, 6]],
        10
    ),
    (
        [[4, 2], [9, 100], [14, 86], [17, 86], [17, 75], [21, 43], [28, 41], [35, 44], [35, 6],
         [42, 14], [56, 74], [65, 58], [70, 6], [72, 37], [74, 33], [75, 56], [87, 84], [97, 43], [99, 12]],
        6
    ),
    (
        [[1, 19], [2, 10], [5, 93], [5, 16], [5, 12], [5, 8], [6, 17], [7, 50], [8, 46], [10, 93], [10, 19], [11, 76], [12, 70], [13, 44], [20, 83], [21, 50], [23, 53], [26, 55], [31, 52], [35, 39], [36, 30], [38, 47], [39, 89], [40, 79], [40, 61], [41, 9], [41, 5], [45, 35], [45, 2], [49, 73], [49, 53], [52, 91], [52, 22], [55, 86], [55, 18], [58, 56], [59, 5], [60, 70], [64, 54], [69, 78], [73, 8], [74, 93], [74, 86], [75, 79], [79, 93], [80, 1], [81, 55], [81, 8], [91, 8], [93, 20], [96, 90], [99, 27], [100, 93]],
        14
    ),
    (
        [[19, 35], [31, 63], [40, 33], [45, 68], [59, 11], [61, 40], [88, 54]],
        3
    ),
    (
        [[1, 60], [2, 1], [3, 56], [4, 43], [4, 26], [4, 24], [5, 95], [5, 74], [5, 59], [6, 7], [7, 84], [8, 99], [9, 19], [11, 20], [12, 97], [12, 91], [12, 31], [12, 27], [12, 9], [13, 36], [15, 35], [15, 3], [16, 25], [18, 42], [19, 73], [19, 31], [19, 17], [20, 98], [21, 45], [22, 51], [22, 35], [23, 46], [24, 19], [25, 76], [26, 92], [29, 64], [30, 82], [30, 35], [31, 77], [32, 44], [32, 13], [33, 22], [33, 19], [37, 40], [40, 87], [41, 98], [41, 30], [42, 51], [42, 34], [44, 30], [48, 95], [48, 77], [49, 81], [54, 92], [54, 88], [54, 19], [56, 96], [57, 99], [57, 19], [58, 66], [58, 20], [59, 99], [61, 27], [63, 16], [66, 89], [66, 1], [67, 59], [69, 73], [72, 45], [73, 27], [75, 23], [75, 7], [76, 58], [77, 1], [78, 39], [79, 22], [80, 41], [81, 65], [82, 86], [82, 83], [83, 77], [85, 86], [86, 83], [89, 64], [89, 47], [93, 24], [95, 23], [95, 14], [96, 47], [97, 73], [97, 17], [98, 35]],
        15
    ),
    (
        [[6, 22], [14, 17], [16, 93], [18, 27], [22, 100], [23, 52], [27, 50], [31, 16], [45, 63], [49, 100], [55, 80], [59, 95], [59, 84], [60, 41], [63, 21], [63, 19], [64, 47], [86, 62], [87, 3], [94, 33], [98, 58]],
        6

    ),
    (
        [[1, 57], [7, 37], [7, 6], [8, 1], [9, 69], [10, 76], [11, 61], [11, 12], [15, 22], [16, 68], [16, 26], [17, 67], [18, 5], [20, 71], [20, 24], [20, 15], [22, 8], [23, 79], [24, 82], [25, 38], [27, 86], [27, 63], [27, 5], [28, 31], [29, 9], [32, 95], [35, 66], [38, 65], [39, 37], [40, 36], [40, 29], [42, 64], [42, 5], [44, 89], [45, 37], [46, 43], [48, 71], [49, 86], [51, 80], [52, 12], [53, 89], [53, 23], [54, 55], [55, 36], [57, 40], [58, 72], [60, 95], [60, 22], [61, 83], [63, 50], [64, 33], [65, 80], [66, 67], [67, 36], [67, 33], [68, 73], [68, 27], [70, 96], [73, 92], [73, 33], [73, 22], [79, 18], [80, 33], [81, 99], [81, 93], [82, 75], [82, 6], [85, 57], [85, 40], [86, 37], [89, 93], [89, 88], [89, 35], [90, 94], [90, 58], [91, 27], [92, 100], [92, 65], [92, 38], [93, 94], [94, 64], [96, 6], [97, 89], [98, 32], [100, 67], [100, 52]],
        15
    ),
    (
        [[6, 45], [6, 9], [9, 88], [10, 10], [15, 39], [17, 61], [19, 95], [20, 69], [21, 54], [22, 35], [23, 46], [24, 51], [24, 19], [28, 78], [29, 35], [30, 45], [37, 16], [37, 5], [39, 18], [40, 20], [41, 21], [44, 48], [45, 48], [46, 94], [47, 39], [47, 6], [52, 88], [53, 7], [54, 74], [55, 82], [58, 91], [64, 53], [64, 16], [65, 84], [65, 73], [66, 95], [67, 58], [70, 30], [75, 6], [76, 26], [77, 74], [80, 53], [81, 13], [82, 73], [83, 87], [84, 4], [85, 50], [86, 68], [86, 21], [87, 75], [88, 74], [90, 32], [91, 57], [93, 72], [93, 54], [94, 69], [95, 28], [98, 9], [99, 19], [100, 68], [100, 21]],
        11
    ),
    (
        [[4, 64], [6, 6], [7, 68], [7, 40], [9, 51], [9, 35], [10, 90], [15, 21], [15, 7], [19, 8], [20, 62], [20, 49], [20, 9], [23, 53], [26, 62], [26, 11], [26, 7], [30, 94], [30, 31], [31, 96], [32, 98], [33, 75], [36, 91], [36, 69], [37, 78], [37, 26], [42, 25], [43, 86], [43, 69], [47, 33], [48, 100], [48, 58], [48, 53], [48, 50], [48, 31], [49, 40], [51, 90], [53, 72], [53, 36], [54, 27], [56, 54], [59, 51], [61, 66], [61, 44], [62, 43], [63, 21], [66, 33], [71, 11], [76, 28], [81, 30], [83, 21], [84, 71], [85, 68], [88, 37], [89, 40], [92, 68], [93, 24], [94, 63], [94, 28], [99, 88], [100, 99]],
        14
    ),
    (
        [[13, 98], [23, 15], [42, 50], [68, 36], [91, 53]],
        3
    )

]

              
sol = Solution()
total_time = 0.0
result = None

for envelopes, expected in test_cases:
    start_time = time.perf_counter()
    result = sol.maxEnvelopes(envelopes)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    assert result == expected, f"Test failed for envelopes={envelopes}. Expected {expected}, got {result}"
    print(f"Test passed for envelopes={envelopes}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")                                                 
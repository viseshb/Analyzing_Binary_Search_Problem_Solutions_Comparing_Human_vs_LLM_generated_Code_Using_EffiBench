#744. Find Smallest Letter Greater Than Target
#https://leetcode.com/problems/find-smallest-letter-greater-than-target/


import time
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)
        while left < right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left % len(letters)]
    

test_cases = [
    (['a', 'p', 'p', 'v', 'y'], 'j','p'),
    (['c', 'e', 'g', 'r', 'y'], 'f', 'g'),
    (['d', 'h', 'j', 'r', 'v'], 'k', 'r'),
    (['c', 'g', 'h', 'k', 'm', 'm', 'n', 'o', 'p', 'w'], 'e', 'g'),
    (['c', 'd', 'd', 'm', 'q', 't', 'v'], 'w','c'),
    (['b', 'h', 'j'], 'y','b'),
    (['d', 'f', 'j', 'j', 'k', 'p', 's', 'u'], 'r','s'),
    (['k', 'n', 'r', 'r'], 'g', 'k'),
    (['a', 'k', 'l', 'q', 's', 'w'], 'h', 'k'),
    (['r', 'x'], 'd', 'r')
]

sol = Solution()
total_time = 0.0

for letters, target, expected in test_cases:
    start_time = time.perf_counter()
    result = sol.nextGreatestLetter(letters, target)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    assert result == expected, f"Test failed for letters({letters}) and target{target}. Expected {expected}, got {result}"
    print(f"Test passed for letters={letters} and target= {target}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds") 

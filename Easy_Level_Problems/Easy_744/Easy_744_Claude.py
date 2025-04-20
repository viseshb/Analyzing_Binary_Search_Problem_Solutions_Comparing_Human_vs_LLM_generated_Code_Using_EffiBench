#744. Find Smallest Letter Greater Than Target
#https://leetcode.com/problems/find-smallest-letter-greater-than-target/


import time
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        n = len(letters)
        
        # If target is greater than or equal to the last letter, return the first letter
        if target >= letters[-1]:
            return letters[0]
        
        left, right = 0, n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If the middle letter is less than or equal to target,
            # search in the right half
            if letters[mid] <= target:
                left = mid + 1
            # Otherwise, search in the left half
            else:
                right = mid
        
        # At this point, letters[left] is the smallest character greater than target
        return letters[left]
        

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

#493. Reverse Pairs
#https://leetcode.com/problems/reverse-pairs/description/


import time 
class Solution:
    def reversePairs(self, nums):
        if not nums:
            return 0
        
        self.count = 0
        self.temp = []
        self.sort_and_count(nums, 0, len(nums) - 1)
        return self.count
    
    def sort_and_count(self, nums, start, end):
        if start >= end:
            return
        
        mid = start + (end - start) // 2
        self.sort_and_count(nums, start, mid)
        self.sort_and_count(nums, mid + 1, end)
        
        # Count reverse pairs using binary search
        j = mid + 1
        for i in range(start, mid + 1):
            # Use binary search to find the first position where nums[j] * 2 >= nums[i]
            j = self.binary_search(nums, j, end + 1, nums[i] / 2.0)
            self.count += j - (mid + 1)
        
        # Merge the sorted arrays
        self.merge(nums, start, mid, end)
    
    def binary_search(self, nums, left, right, target):
        # Find the first position where nums[pos] > target
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left
    
    def merge(self, nums, start, mid, end):
        # Standard merge operation
        self.temp = [0] * (end - start + 1)
        i, j, k = start, mid + 1, 0
        
        while i <= mid and j <= end:
            if nums[i] <= nums[j]:
                self.temp[k] = nums[i]
                i += 1
            else:
                self.temp[k] = nums[j]
                j += 1
            k += 1
        
        while i <= mid:
            self.temp[k] = nums[i]
            i += 1
            k += 1
        
        while j <= end:
            self.temp[k] = nums[j]
            j += 1
            k += 1
        
        for k in range(len(self.temp)):
            nums[start + k] = self.temp[k]

test_cases = [
    ([2999, 9333, 2036, 3150, 9883, 634, 5863, 3735],9),
    ([3148, 4810, 4271] ,0),
    ([3158, 2407, 3804, 5887, 6286, 2865, 3796, 1514, 4115, 8274, 7916, 8582, 8268, 9522, 3159, 6095, 3663, 4693, 1192, 5534, 9789, 9722, 885, 857, 2352, 5407, 6342, 875, 4292, 6882, 9786, 1876, 8209, 7345, 3626, 595, 4731, 9137, 2737, 3687, 1301, 3105, 7380, 4408, 6453, 7105, 4674, 8419, 3719, 7572, 2162, 8389, 4527, 8128, 4978, 2810, 2232, 8178],355),
    ([4957, 565, 2177, 1876, 2785, 608, 5050, 9502, 3789, 639, 4474, 8604, 4853, 3905, 3209, 4522, 3994, 2049, 4695], 31),
    ([7598, 9455, 8240, 6109, 5064, 889, 512, 5867, 391, 3571, 8397, 4413, 1049, 1488, 5764, 4907, 698, 7175, 198, 1021, 6852, 5926, 4776, 72, 534, 7854, 5054, 5890, 7732, 4712, 2807, 7780, 223, 1512, 373, 2038, 8998, 7529, 9629, 8992, 5590, 6046, 7080, 2568, 7147, 8997, 8990, 5579, 9730, 3293, 867, 7629, 8637, 1199, 3010, 8086, 2530, 3339, 7677, 5225, 2709, 5406, 4002], 458),
    ([2863, 7643, 6912, 6518, 8790, 3466, 368, 5229, 1769, 4604, 6694, 7029, 5025, 8676, 7166, 1918, 8143, 521, 8064, 4638, 679, 4771, 1608, 4175, 669, 9755, 8670, 5545, 1724, 4, 5574, 8377, 3130, 2454, 6041, 1381, 2721, 2092, 6247, 6748, 6428, 2858, 1123, 6182, 6380, 3782, 1132, 392, 2911, 5471, 582, 4663, 108, 3665, 1879, 2378, 9997, 3044, 7823, 8600, 59, 8068, 4954, 5416],624),
    ([5781, 423, 5733, 5475, 8932, 3206, 3879, 7697, 7603, 8557, 1960, 6978, 9319, 5063, 7748, 4254, 6381, 8563, 4024, 6211, 506, 6083, 2197, 2617, 2008, 4639, 8939, 3480, 6158, 7458, 88, 3784, 8919, 9662, 1468, 3757, 749, 7949, 5786, 8161, 7365, 4696, 9899, 1996, 3860, 8429, 5131, 6654, 3690, 6564, 8273, 2409, 643, 2239, 3631, 6511, 9545, 3655, 7352, 4694, 2889], 432),
    ([9089, 1613, 7946, 120, 960, 6439, 4514, 3874, 8068, 8715, 9038, 4310, 1909, 1950, 9683, 7353, 89, 9066, 1293, 2266, 3690, 6606, 3991, 4088, 7365, 9130, 8959, 7683, 6468, 546, 1103, 878, 6291, 9257, 4557, 8041, 8653, 3301, 3163, 4901, 648, 7015, 6547, 8566, 2442, 8777], 248),
    ([8029, 7745, 1077, 524, 4606, 5759, 2061, 7702, 9494, 5232, 4755, 7518, 9809, 8363, 8660, 3194, 5890, 7993, 8532, 3898, 7961, 3839, 1686, 8358, 7529, 3976, 1356, 3022, 7613, 87, 6426, 7675, 5513, 2728, 7781, 4630, 7968, 4362, 4033, 7525],154),
    ([7595, 2044, 4197, 5295, 7391, 8091, 5547, 5359, 8783, 4551, 560, 77, 8011, 620, 1683, 5061, 8295, 6044, 4296, 2086, 1666, 606, 3485, 6061, 5333, 3795, 4806, 8027, 7488, 2101, 3839, 9841, 2790, 9753, 7093, 8249, 5203, 1994, 1849, 9989, 1786, 2467, 9049, 8061, 3129, 2041, 2990, 2849, 6687, 9692, 5416, 2512, 2954, 4674], 358)
]

sol = Solution()
total_time = 0.0

for nums, expected in test_cases:
    start_time = time.perf_counter()
    result = sol.reversePairs(nums)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    assert result == expected, f"Test failed for nums({nums}). Expected {expected}, got {result}"
    print(f"Test passed for nums={nums}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")

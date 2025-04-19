import time
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Number of papers with at least citations[mid] citations
            papers_with_citations = n - mid
            
            # If we have enough papers with at least this many citations
            if citations[mid] >= papers_with_citations:
                # We might find a better h-index by moving left
                right = mid - 1
            else:
                # We need more citations, move right
                left = mid + 1
        
        # At this point, left is the first position where citations[left] >= n - left
        # So n - left is our h-index
        return n - left


# Create an instance of the Solution class
solution = Solution()

test_cases = [
    ([14, 99, 145, 159, 183, 184, 249, 265, 281, 293, 307, 311, 341, 345, 350, 366, 403, 441, 454, 504, 520, 528, 557, 563, 624, 647, 665, 666, 679, 709, 730, 751, 755, 819, 849, 856, 886, 890, 891, 901, 906, 927, 935, 941, 999], 44),
    ([8, 57, 60, 132, 239, 336, 379, 436, 681, 790, 840, 843, 850, 943, 969], 14),
    ([29, 33, 50, 57, 126, 146, 205, 338, 364, 401, 415, 430, 433, 466, 525, 530, 532, 535, 560, 570, 590, 633, 635, 663, 669, 747, 773, 778, 841, 896, 915, 934, 976], 32),
    ([3, 13, 33, 36, 39, 52, 56, 71, 104, 120, 127, 128, 163, 185, 193, 194, 195, 198, 204, 209, 231, 250, 253, 256, 266, 269, 286, 291, 293, 320, 325, 332, 349, 354, 370, 378, 384, 387, 391, 402, 409, 426, 438, 439, 452, 476, 482, 488, 491, 492, 495, 498, 500, 503, 506, 518, 523, 526, 535, 565, 576, 581, 592, 614, 621, 631, 637, 638, 649, 657, 664, 681, 688, 689, 697, 758, 791, 796, 799, 804, 836, 837, 840, 852, 865, 870, 871, 898, 911, 913, 918, 921, 936, 942, 946, 961, 963, 965, 996], 91),
    ([37, 55, 112, 157, 342, 376, 456, 495, 568, 607, 628, 651, 687, 703, 723, 724, 760, 829, 839, 909, 928, 946, 989], 23),
    ([7, 26, 53, 55, 63, 85, 92, 96, 152, 165, 167, 202, 218, 225, 286, 323, 341, 362, 363, 366, 369, 379, 399, 449, 452, 459, 463, 471, 472, 525, 537, 539, 554, 563, 586, 607, 614, 621, 650, 653, 659, 673, 717, 731, 752, 765, 766, 776, 800, 839, 961, 974, 986], 51),
    ([15, 32, 39, 66, 72, 97, 98, 104, 111, 129, 148, 153, 159, 161, 165, 173, 194, 196, 208, 213, 222, 224, 238, 240, 248, 266, 267, 273, 279, 296, 300, 305, 319, 329, 336, 345, 365, 370, 384, 393, 426, 433, 437, 457, 472, 474, 475, 545, 554, 564, 581, 582, 600, 612, 615, 624, 625, 631, 643, 672, 704, 707, 709, 753, 775, 787, 800, 803, 825, 836, 845, 848, 852, 870, 891, 918, 921, 922, 941, 948, 950, 961, 970, 980, 985, 1000], 81),
    ([176, 397, 577, 580, 630, 724], 6),
    ([55, 56, 126, 214, 401, 470, 588, 590, 597, 611, 628, 651, 737, 874, 877], 15),
    ([11, 19, 22, 35, 36, 100, 101, 118, 125, 142, 144, 149, 161, 185, 210, 216, 264, 303, 304, 311, 316, 330, 360, 392, 402, 409, 412, 420, 432, 443, 450, 515, 530, 556, 566, 638, 642, 650, 663, 682, 687, 712, 784, 795, 797, 833, 861, 876, 891, 896, 944, 952, 976, 978, 991, 994], 51),
    ([1, 32, 48, 68, 148, 226, 246, 271, 287, 288, 309, 333, 346, 506, 558, 650, 685, 688, 732, 796, 846, 911, 965], 22)
]

total_time = 0.0

for idx, (nums, expected) in enumerate(test_cases, 1):
    start_time = time.perf_counter()
    result = solution.hIndex(nums)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time

    assert result == expected, f"Test failed for nums={nums}. Expected {expected}, got {result}"
    print(f"Test {idx} passed for nums={nums}. Execution time: {execution_time:.12f} seconds")

print(f"\nAll test cases passed successfully!")
print(f"Total execution time for all test cases: {total_time:.12f} seconds")

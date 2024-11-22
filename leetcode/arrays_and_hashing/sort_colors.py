from typing import List


# Bucket Sort
# Time Complexity: O(n)
# Space Complexity: 0(1)
# n - Number of elements in nums
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0, 0, 0]

        for num in nums:
            counts[num] += 1

        i = 0
        for num in range(len(counts)):
            for _ in range(counts[num]):
                nums[i] = num
                i += 1


# Two Pointers / Dutch National Flag algorithm
# Time Complexity: O(n), one-pass
# Space Complexity: 0(1)
# n - Number of elements in nums
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        l = 0
        r = len(nums) - 1

        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                continue
            i += 1

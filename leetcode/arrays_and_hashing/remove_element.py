from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0

        while i < len(nums):
            if nums[i] == val:
                nums[i], nums[-1] = nums[-1], nums[i]
                nums.pop()
                continue
            i += 1

        return len(nums)

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         l = 0
#         r = len(nums) - 1
#
#         while l <= r:
#             if nums[l] == val:
#                 nums[l], nums[r] = nums[r], nums[l]
#                 r -= 1
#                 continue
#             l += 1
#
#         return l


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         k = 0
#
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k += 1
#
#         return k

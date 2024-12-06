import bisect
from typing import List


# Iterative Binary Search
# Time Complexity: O(log(n))
# Space Complexity: O(1)
# n - Number of elements in nums
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m

        return -1


# Recursive Binary Search
# Time Complexity: O(log(n))
# Space Complexity: O(log(n))
# n - Number of elements in nums
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.__binary_search(nums, 0, len(nums) - 1, target)

    def __binary_search(self, nums, l, r, target):
        if l > r:
            return -1

        m = l + (r - l) // 2

        if target == nums[m]:
            return m
        elif target > nums[m]:
            return self.__binary_search(nums, m + 1, r, target)
        else:
            return self.__binary_search(nums, l, m - 1, target)


# Upper Bound
# Time Complexity: O(log(n))
# Space Complexity: O(1)
# n - Number of elements in nums
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            m = (l + r) // 2
            if target >= nums[m]:
                l = m + 1
            else:
                r = m

        if l > 0 and target == nums[l - 1]:
            return l - 1
        else:
            return -1


# Lower Bound
# Time Complexity: O(log(n))
# Space Complexity: O(1)
# n - Number of elements in nums
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            m = l + (r - l) // 2
            if target <= nums[m]:
                r = m
            else:
                l = m + 1

        if l < len(nums) and target == nums[l]:
            return l
        else:
            return -1


# Upper Bound using built-in "bisect" module
# Time Complexity: O(log(n))
# Space Complexity: O(1)
# n - Number of elements in nums
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect.bisect_right(nums, target)

        if i > 0 and target == nums[i - 1]:
            return i - 1
        else:
            return -1


# Lower Bound using built-in "bisect" module
# Time Complexity: O(log(n))
# Space Complexity: O(1)
# n - Number of elements in nums
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect.bisect_left(nums, target)

        if i < len(nums) and target == nums[i]:
            return i
        else:
            return -1

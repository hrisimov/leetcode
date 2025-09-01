from typing import List


# Sorting
# Time Complexity: O(n * log(n) + n) => O(n * log(n))
# Space Complexity: O(log(n)) or O(n) space depending on the sorting algorithm
# where:
#   - n is the length of the input array
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False


# Hash Set I
# Time Complexity: O(n)
# Space Complexity: O(n)
# where:
#   - n is the length of the input array
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()

        for num in nums:
            if num in unique_nums:
                return True
            unique_nums.add(num)

        return False


# Hash Set II
# Time Complexity: O(n)
# Space Complexity: O(n)
# where:
#   - n is the length of the input array
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

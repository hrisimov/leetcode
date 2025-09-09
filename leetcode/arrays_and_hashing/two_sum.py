from typing import List


# Brute Force
# Time Complexity: O(n ^ 2)
# Space Complexity: O(1)
# where:
#   - n is the length of the input array
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)

        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []


# Sorting + Two Pointers
# Time Complexity: O(n + n * log(n) + n) => O(n * log(n))
# Space Complexity: O(log(n)) or O(n) space depending on the sorting algorithm
# where:
#   - n is the length of the input array
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            nums[i] = [num, i]

        nums.sort()
        i = 0
        j = len(nums) - 1

        while i < j:
            current_sum = nums[i][0] + nums[j][0]
            if current_sum > target:
                j -= 1
            elif current_sum < target:
                i += 1
            else:
                return [nums[i][1], nums[j][1]]

        return []


# Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)
# where:
#   - n is the length of the input array
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_nums = {}

        for i, num in enumerate(nums):
            # num + x = target => x = target - num
            if target - num in visited_nums:
                return [visited_nums[target - num], i]
            visited_nums[num] = i

        return []

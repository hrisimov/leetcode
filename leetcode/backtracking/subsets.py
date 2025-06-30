from typing import List


# Recursion with backtracking I
# Time Complexity: O(n * 2 ^ n)
# Space Complexity:
#   - O(n * 2 ^ n) space for the output array
#   - O(n) space for the `subset` array
#   - O(n) space for the recursion stack
# where:
#   - n is the length of the input array
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        nums_len = len(nums)

        def subsets_internal(i):
            result.append(subset[:])

            for j in range(i, nums_len):
                subset.append(nums[j])
                subsets_internal(j + 1)
                subset.pop()

        subsets_internal(0)
        return result


# Recursion with backtracking II
# Time Complexity: O(2 ^ n + n * 2 ^ n) => O(n * 2 ^ n)
# Space Complexity:
#   - O(n * 2 ^ n) space for the output array
#   - O(n) space for the `subset` array
#   - O(n) space for the recursion stack
# where:
#   - n is the length of the input array
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        nums_len = len(nums)

        def dfs(i):
            if i == nums_len:
                result.append(subset[:])
                return

            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result


# Recursion
# Time Complexity: O(n * 2 ^ n)
# Space Complexity:
#   - O(n * 2 ^ n) space for the output array
#   - O(n) space for the recursion stack
# where:
#   - n is the length of the input array
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)

        def subsets_internal(i):
            if i == nums_len:
                return [[]]

            result = subsets_internal(i + 1)

            for j in range(len(result)):
                result.append(result[j][:])
                result[-1].append(nums[i])

            return result

        return subsets_internal(0)


# Iteration
# Time Complexity: O(n * 2 ^ n)
# Space Complexity:
#   - O(n * 2 ^ n) space for the output array
#   - O(1) extra space
# where:
#   - n is the length of the input array
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            for i in range(len(result)):
                result.append(result[i] + [num])

        return result

from typing import List


# Recursion with backtracking
# Time Complexity: O(2 ^ (k + n) + c * k)
# Space Complexity:
#   - O(c * k) space for the output array
#   - O(k) space for the `combination` array
#   - O(k + n) space for the recursion stack
# where:
#   - k = t / m
#   - t is the `target` input integer
#   - m is the min value from the input array
#   - n is the length of the input array
#   - c is the count of combinations that sum up to `target`
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []
        candidates_len = len(candidates)

        def dfs(i, target):
            if target < 0 or i == candidates_len:
                return

            if target == 0:
                result.append(combination[:])
                return

            combination.append(candidates[i])
            dfs(i, target - candidates[i])
            combination.pop()
            dfs(i + 1, target)

        dfs(0, target)
        return result


# Recursion with backtracking and pruning
# Time Complexity: O(n * log(n) + n ^ k + c * k)
# Space Complexity:
#   - O(log(n)) or O(n) space depending on the sorting algorithm
#   - O(c * k) space for the output array
#   - O(k) space for the `combination` array
#   - O(k) space for the recursion stack
# where:
#   - k = t / m
#   - t is the `target` input integer
#   - m is the min value from the input array
#   - n is the length of the input array
#   - c is the count of combinations that sum up to `target`
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        combination = []
        candidates_len = len(candidates)

        def dfs(i, target):
            if target == 0:
                result.append(combination[:])
                return

            for j in range(i, candidates_len):
                if target - candidates[j] < 0:
                    return
                combination.append(candidates[j])
                dfs(j, target - candidates[j])
                combination.pop()

        dfs(0, target)
        return result

from typing import List


# Recursion with backtracking
# Time Complexity: O(2 ^ (k + n) + k * 2 ^ (k + n)) => O(k * 2 ^ (k + n))
# Space Complexity:
#   - O(k * 2 ^ (k + n)) space for the output array
#   - O(k) space for the `combination` array
#   - O(k + n) space for the recursion stack
# where:
#   - k = t / m
#   - t is the `target` input integer
#   - m is the min value from the input array
#   - n is the length of the input array
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
# Time Complexity: O(n * log(n) + n ^ k + k * n ^ k) => O(n * log(n) + k * n ^ k)
# Space Complexity:
#   - O(k * n ^ k) space for the output array
#   - O(k) space for the `combination` array
#   - O(k) space for the recursion stack
# where:
#   - k = t / m
#   - t is the `target` input integer
#   - m is the min value from the input array
#   - n is the length of the input array
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        combination = []
        candidates_len = len(candidates)

        def dfs(i, target):
            for j in range(i, candidates_len):
                target -= candidates[j]

                if target < 0:
                    return
                elif target == 0:
                    result.append(combination + [candidates[j]])
                    return

                combination.append(candidates[j])
                dfs(j, target)
                combination.pop()
                target += candidates[j]

        dfs(0, target)
        return result

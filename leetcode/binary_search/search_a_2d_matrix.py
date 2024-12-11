from typing import List


# Binary Search
# Time Complexity: O(log(m) + log(n)) => O(log(m * n))
# Space Complexity: O(1)
# m - Number of lists in matrix (rows)
# n - Number of elements in each list (columns)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                break
        else:
            return False

        row = matrix[m]
        l = 0
        r = len(row) - 1

        while l <= r:
            m = (l + r) // 2
            if target > row[m]:
                l = m + 1
            elif target < row[m]:
                r = m - 1
            else:
                return True

        return False


# Binary Search (one pass)
# Time Complexity: O(log(m * n))
# Space Complexity: O(1)
# m - Number of lists in matrix (rows)
# n - Number of elements in each list (columns)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols - 1

        while l <= r:
            m = (l + r) // 2
            row = m // cols
            col = m % cols

            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True

        return False

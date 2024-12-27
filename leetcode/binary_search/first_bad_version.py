# Sample 'isBadVersion' implementation
def isBadVersion(version):
    return version >= 4


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


# Binary Search - Variant 1
# Time Complexity: O(log(k))
# Space Complexity: O(1)
# k - Size of the search space (from 1 to n)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                if m == 1 or not isBadVersion(m - 1):
                    return m
                r = m - 1
            else:
                l = m + 1


# Binary Search - Variant 2
# Time Complexity: O(log(k))
# Space Complexity: O(1)
# k - Size of the search space (from 1 to n)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1

        return l

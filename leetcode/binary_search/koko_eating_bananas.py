from math import ceil
from typing import List


# Binary Search
# Time Complexity: O(n + n + n * log(m))
# Space Complexity: O(1)
# n - Count of piles
# m - Length of the range between min and max bananas-per-hour eating speed
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = ceil(sum(piles) / h)
        r = max(piles)

        while l <= r:
            m = l + (r - l) // 2
            needed_hours = sum(ceil(p / m) for p in piles)

            if needed_hours > h:
                l = m + 1
            else:
                r = m - 1

        return l

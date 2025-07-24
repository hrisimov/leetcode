import heapq
from typing import List


# Sorting + Binary Search
# Time Complexity: O(n * log(n) + m * (log(n + m) + n + m)) => O(m ^ 2 + m * n)
# Space Complexity:
#   - O(log(n)) or O(n) space depending on the sorting algorithm
#   - O(n + m) space for the max length of the `nums` array
# where:
#   - n is the initial length of the `nums` array
#   - m is the number of calls made to the `add` method
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k - 1
        self.nums = nums
        self.nums.sort(reverse=True)

    def add(self, val: int) -> int:
        l = 0
        r = len(self.nums) - 1

        while l <= r:
            m = (l + r) // 2
            if val > self.nums[m]:
                r = m - 1
            elif val < self.nums[m]:
                l = m + 1
            else:
                self.nums.insert(m, val)
                return self.nums[self.k]

        self.nums.insert(l, val)
        return self.nums[self.k]


# Min Heap
# Time Complexity: O(n * log(k) + m * log(k)) => O((n + m) * log(k))
# Space Complexity: O(k)
# where:
#   - n is the length of the `nums` array
#   - m is the number of calls made to the `add` method
#   - k is the max length of the heap
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.nums_heap) < self.k:
            heapq.heappush(self.nums_heap, val)
        elif val > self.nums_heap[0]:
            heapq.heappush(self.nums_heap, val)
            heapq.heappop(self.nums_heap)

        return self.nums_heap[0]

import heapq
from typing import List


# Sorting + Binary Search
# Time Complexity: O(n * log(n) + n ^ 2) => O(n ^ 2)
# Space Complexity:
#   - O(log(n)) or O(n) space depending on the sorting algorithm
#   - O(log(n) space for the recursion stack
# where:
#   - n is the length of the input array
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            first = stones.pop()
            second = stones.pop()
            if first == second:
                continue
            stones.insert(
                self.__find_insert_position(stones, first - second),
                first - second
            )

        return stones[0] if stones else 0

    @staticmethod
    def __find_insert_position(values, target):
        def binary_search(l, r):
            if l > r:
                return l

            m = l + (r - l) // 2

            if target == values[m]:
                return m
            elif target > values[m]:
                return binary_search(m + 1, r)
            else:
                return binary_search(l, m - 1)

        return binary_search(0, len(values) - 1)


# Max Heap
# Time Complexity: O(n + n + n * log(n)) => O(n * log(n))
# Space Complexity: O(1)
# where:
#   - n is the length of the input array
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for index, value in enumerate(stones):
            stones[index] = -value

        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first == second:
                continue
            heapq.heappush(stones, first - second)

        return -stones[0] if stones else 0


# Bucket Sort
# Time Complexity: O(n + m + n + m) => O(n + m)
# Space Complexity: O(m)
# where:
#   - n is the length of the input array
#   - m is the max value in the input array
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_count = self.__bucket_sort(stones)
        first = len(stones_count) - 1
        second = first - 1

        while first > 0:
            if stones_count[first] % 2 == 0:
                first -= 1
                continue

            second = min(first - 1, second)

            while second > 0 and stones_count[second] == 0:
                second -= 1

            if second == 0:
                break

            stones_count[first] -= 1
            stones_count[second] -= 1
            stones_count[first - second] += 1
            first = max(first - second, second)

        return first

    @staticmethod
    def __bucket_sort(values):
        result = [0] * (max(values) + 1)

        for value in values:
            result[value] += 1

        return result

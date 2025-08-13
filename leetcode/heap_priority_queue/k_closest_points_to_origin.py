import heapq
import math
import random
from typing import List


def calculate_distance_between_points(point1, point2=None):
    if not point2:
        point2 = [0, 0]

    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # Euclidean distance


# Sorting
# Time Complexity: O(n * log(n) + k) => O(n * log(n))
# Space Complexity:
#   - O(log(n)) or O(n) space depending on the sorting algorithm
#   - O(k) space for the output array
# where:
#   - n is the length of the input array
#   - k is the length of the output array
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=calculate_distance_between_points)
        return points[:k]


# Min Heap
# Time Complexity: O(n + n + k * log(n)) => O(k * log(n))
# Space Complexity:
#   - O(k) space for the output array
# where:
#   - n is the length of the input array
#   - k is the length of the output array
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for index, point in enumerate(points):
            points[index] = [
                calculate_distance_between_points(point),
                point
            ]

        heapq.heapify(points)
        return [heapq.heappop(points)[1] for _ in range(k)]


# Max Heap
# Time Complexity: O(n * log(k) + k * log(k)) => O(n * log(k))
# Space Complexity:
#   - O(k) space for the heap
#   - O(k) space for the output array
# where:
#   - n is the length of the input array
#   - k is the length of the heap / output array
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_heap = []
        for point in points:
            distance = -calculate_distance_between_points(point)
            if len(points_heap) < k:
                heapq.heappush(points_heap, [distance, point])
            elif distance > points_heap[0][0]:
                heapq.heappush(points_heap, [distance, point])
                heapq.heappop(points_heap)

        result = []
        while points_heap:
            result.append(heapq.heappop(points_heap)[1])

        return result


"""
Quick Select
--------------------------------------------------------------------
                   |    Time Complexity    |     Space Complexity
--------------------------------------------------------------------
    Best Case      |         O(n)          |          O(k)
                   |                       |
   Average Case    |         O(n)          |          O(k)
                   |                       |
    Worst Case     |       O(n ^ 2)        |          O(k)
--------------------------------------------------------------------
where:
    - n is the length of the input array
    - k is the length of the output array
"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = 0
        r = len(points) - 1
        p = len(points)

        while True:
            if p == k:
                break
            elif p < k:
                l = p + 1
            else:
                r = p - 1
            p = self.__randomized_partition(points, l, r)

        return points[:k]

    @staticmethod
    def __randomized_partition(points, l, r):
        p = random.randint(l, r)
        points[p], points[r] = points[r], points[p]

        j = l
        pivot_distance = calculate_distance_between_points(points[r])

        for i in range(l, r):
            if calculate_distance_between_points(points[i]) <= pivot_distance:
                points[j], points[i] = points[i], points[j]
                j += 1

        points[j], points[r] = points[r], points[j]
        return j

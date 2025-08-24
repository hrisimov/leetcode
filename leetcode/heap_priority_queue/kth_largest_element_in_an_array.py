import heapq
import random
from typing import List


# Min Heap I
# Time Complexity: O(n * log(k))
# Space Complexity: O(k)
# where:
#   - n is the length of the input array
#   - k is the length of the heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_heap = []

        for num in nums:
            if len(nums_heap) < k:
                heapq.heappush(nums_heap, num)
            elif num > nums_heap[0]:
                heapq.heappush(nums_heap, num)
                heapq.heappop(nums_heap)

        return nums_heap[0]


# Min Heap II
# Time Complexity: O(n * log(k))
# Space Complexity: O(k)
# where:
#   - n is the length of the input array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


# Max Heap
# Time Complexity: O(n + n + k * log(n)) => O(k * log(n))
# Space Complexity: O(1)
# where:
#   - n is the length of the input array / heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i, num in enumerate(nums):
            nums[i] = -num

        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)

        return -nums[0]


"""
Quick Select I
--------------------------------------------------------------------
                   |    Time Complexity    |     Space Complexity
--------------------------------------------------------------------
    Best Case      |         O(n)          |          O(1)
                   |                       |
   Average Case    |         O(n)          |          O(1)
                   |                       |
    Worst Case     |       O(n ^ 2)        |          O(1)
--------------------------------------------------------------------
where:
    - n is the length of the input array
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k -= 1
        left = 0
        right = len(nums) - 1

        while True:
            if right <= left + 1:
                if right == left + 1 and nums[left] < nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]
                return nums[k]

            p = self.__partition(nums, left, right)

            if k < p:
                right = p - 1
            elif k > p:
                left = p + 1
            else:
                return nums[k]

    @staticmethod
    def __partition(nums, left, right):
        mid = left + (right - left) // 2
        nums[left + 1], nums[mid] = nums[mid], nums[left + 1]
        nums[left], nums[left + 1], nums[right] = sorted([nums[left], nums[left + 1], nums[right]], reverse=True)

        pivot = nums[left + 1]
        i = left + 1
        j = right

        while True:
            while True:
                i += 1
                if nums[i] <= pivot:
                    break
            while True:
                j -= 1
                if nums[j] >= pivot:
                    break
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[left + 1], nums[j] = nums[j], nums[left + 1]
        return j


"""
Quick Select II
--------------------------------------------------------------------
                   |    Time Complexity    |     Space Complexity
--------------------------------------------------------------------
    Best Case      |         O(n)          |          O(1)
                   |                       |
   Average Case    |         O(n)          |          O(1)
                   |                       |
    Worst Case     |       O(n ^ 2)        |          O(1)
--------------------------------------------------------------------
where:
    - n is the length of the input array
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k -= 1
        left = 0
        right = len(nums) - 1

        while True:
            mid_left, mid_right = self.__partition(nums, left, right)
            if k < mid_left:
                right = mid_left - 1
            elif k > mid_right:
                left = mid_right + 1
            else:
                return nums[k]

    @staticmethod
    def __partition(nums, left, right):
        p = random.randint(left, right)
        nums[p], nums[right] = nums[right], nums[p]

        pivot = nums[right]
        i = left
        mid_left = left
        mid_right = right

        while i <= mid_right:
            if nums[i] > pivot:
                nums[mid_left], nums[i] = nums[i], nums[mid_left]
                mid_left += 1
            elif nums[i] < pivot:
                nums[i], nums[mid_right] = nums[mid_right], nums[i]
                mid_right -= 1
                continue
            i += 1

        return mid_left, mid_right
